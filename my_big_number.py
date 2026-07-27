"""Core class for adding large non-negative integers written as strings."""

from __future__ import annotations

import logging


logger = logging.getLogger(__name__)


class MyBigNumber:
    """Add large numbers using the same right-to-left carry method taught in school."""

    def sum(self, stn1: str, stn2: str) -> str:
        """Return stn1 + stn2.

        Inputs are assumed to contain only valid decimal digits.
        """
        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0
        result: list[str] = []
        step = 1

        while i >= 0 or j >= 0 or carry > 0:
            digit1 = int(stn1[i]) if i >= 0 else 0
            digit2 = int(stn2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry

            result_digit = total % 10
            next_carry = total // 10
            result.append(str(result_digit))

            logger.info(
                "Step %s: %s + %s + carry %s = %s; write %s, next carry %s",
                step,
                digit1,
                digit2,
                carry,
                total,
                result_digit,
                next_carry,
            )

            carry = next_carry
            i -= 1
            j -= 1
            step += 1

        answer = "".join(reversed(result))
        logger.info("Result: %s + %s = %s", stn1, stn2, answer)
        return answer
