import asyncio
from numbers import Number

from typing import Callable, List

import functools


class Event(object):

    """An event class.
    """

    def __init__(self):
        self._handlers = []  # type: List[HandlerContainer]

    def connect(self, handler: Callable[..., None], immediate: bool = False, once: bool = False,
                ignore_args: bool = False) -> None:
        """
        Connect function `handler` to the event. `handler` is invoked with the same arguments (and keyword arguments) as
        what the event is fired with.
        :param handler: The function to connect to the event.
        :param immediate: Whether the function should be called immediately after the event is fired, or queued onto the
        event loop.
        :param once: Whether the function should only connect once, and automatically disconnect after it is called
        once.
        :param ignore_args: Whether the function should be called with no arguments, ignoring the arguments the event
        was fired with.
        :return: None
        """
        if asyncio.iscoroutinefunction(handler) and immediate:
            raise ValueError('Can\'t connect coroutine function with immediate=True')

        self._handlers.append(HandlerContainer(handler, immediate=immediate, once=once, ignore_args=ignore_args))

    def disconnect(self, handler: Callable[..., None]) -> None:
        """Disconnect `handler` from this event.
        :param handler: Event handler to disconnect.
        :return: None
        """
        for container in self._handlers:
            if container.handler == handler:
                self._handlers.remove(container)
                break
        else:
            raise HandlerNotConnected

    def fire(self, *args, **kwargs) -> None:
        """Fire the event, any arguments are passed through to event handlers
        :return: None
        """
        for container in self._handlers:
            handler = container.handler

            if container.ignore_args:
                args = []
                kwargs = {}

            if container.immediate:
                handler(*args, **kwargs)
            elif asyncio.iscoroutinefunction(handler):
                asyncio.get_event_loop().create_task(handler(*args, **kwargs))
            else:
                asyncio.get_event_loop().call_soon(functools.partial(handler, *args, **kwargs))

            container.remaining -= 1

            if container.remaining == 0:
                self.disconnect(handler)

    def fire_ignore_args(self, *args, **kwargs):
        """Same as `Event.fire()` but any arguments passed are ignored. Useful for when using as a callback for other
        third-party functions where you want to ignore the callback arguments. Similar to connecting the handlers with
        `ignore_args=True` but this allows handlers to be transparent to the fact that arguments are being ignored.
        :return: None
        """
        self.fire()


class HandlerContainer:

    """Utility class for storing connect arguments of handlers which affect callback behaviour.
    """

    def __init__(self, handler: Callable[..., None], immediate: bool = False, once: bool = False,
                 ignore_args: bool = False) -> None:

        self.handler = handler  # type: Callable[..., None]
        self.immediate = immediate  # type: bool
        self.ignore_args = ignore_args  # type: bool
        self.remaining = 1 if once else float('inf')  # type: Number


class HandlerNotConnected(Exception):
    pass
