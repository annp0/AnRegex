# AnRegex: A Regex Engine w/ NFAs

## Implemented features

- Concatentation: `ab` matches the subexpression `a`, then `b`;
- Alternation: `a|b` matches either subexpression `a` or `b`;
- Repetition: `a*` will match the string that repeat `a` zero or many times;
- Subexpression: `(a)`, quote a subexpression
- Matcher a character: `x`, `.` match a literal character, and an arbitrary character, respectively.