from typing import List, Tuple, Union, Callable, Any, Optional, Type, TypeVar as _TypeVar
from beaupy import confirm as _confirm, select as _select, select_multiple as _select_multiple, prompt as _prompt
from rich.console import Console as _Console

_TargetType = _TypeVar('_TargetType')

console = _Console()

# === STYLE CONSTANTS ===
_cursor = ">"
_cursor_style = "bright_cyan"

_tick_character = "*"
_tick_style = "bright_cyan"

# === PROMPTS ===

def confirm_prompt(
    question: str,
    default_is_yes: bool = False,
) -> Optional[bool]:
    return _confirm(
        question,
        enter_empty_confirms=False,
        default_is_yes=default_is_yes,
        cursor=_cursor,
        cursor_style=_cursor_style,
        char_prompt=True
    )


def select_prompt(
    question: str,
    options: List[Union[Tuple[int, ...], str]],
    preprocessor: Callable[[Any], Any] = lambda val: val,
    strict: bool = False,
    pagination: bool = False,
    page_size: int = 5
) -> Union[int, Any, None]:
    console.print(question + "?")

    return _select(
        options,
        preprocessor=preprocessor,
        cursor=_cursor,
        cursor_style=_cursor_style,
        strict=strict,
        pagination=pagination,
        page_size=page_size
    )


def select_multiple_prompt(
    question: str,
    options: List[Union[Tuple[int, ...], str]],
    preprocessor: Callable[[Any], Any] = lambda val: val,
    ticked_indices: Optional[List[int]] = None,
    minimal_count: int = 0,
    maximal_count: Optional[int] = None,
    strict: bool = False,
    pagination: bool = False,
    page_size: int = 5,
) -> List[Union[int, Any]]:
    console.print(question + "?")

    return _select_multiple(
        options,
        preprocessor=preprocessor,
        tick_character=_tick_character,
        tick_style=_tick_style,
        cursor_style=_cursor_style,
        ticked_indices=ticked_indices,
        minimal_count=minimal_count,
        maximal_count=maximal_count,
        strict=strict,
        pagination=pagination,
        page_size=page_size
    )


def prompt_input(
    prompt_text: str,
    target_type: Type[_TargetType] = str,
    validator: Callable[[_TargetType], bool] = lambda _: True,
    secure: bool = False,
    raise_validation_fail: bool = True,
    raise_type_conversion_fail: bool = True,
    initial_value: Optional[str] = None,
    completion: Optional[Callable[[str], List[str]]] = None
) -> _TargetType:
    return _prompt(
        prompt_text,
        target_type=target_type,
        validator=validator,
        secure=secure,
        raise_validation_fail=raise_validation_fail,
        raise_type_conversion_fail=raise_type_conversion_fail,
        initial_value=initial_value,
        completion=completion
    )
