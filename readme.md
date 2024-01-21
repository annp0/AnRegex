# AnRegex: A Regex Engine with Nondeterministic Finite Automata

## Implemented features

Composite Operations:
- Concatentation: `ab` matches the subexpression `a`, then `b`;
- Alternation: `a|b` matches either subexpression `a` or `b`;
- Repetition: `a*` matches the string that repeat `a` zero or many times;
- Quotation: `(a)` quotes a subexpression

Atomic Operations:
- : `x` matches a literal character
- : `.` matches any single character

The priority (from high to low) is: 1. Parenthesis, 2. Union, 3. Repetition 4. Concatenation

The above basic operations are able to express all operations that are supported by the google re2 engine.

## Manual

First, import the `regex` module. Initialize a instance by
```
re = regex(string) 
```
where `string` is the regular expression. First, `regex` will detect whether the expression is legal with the `error` module.

After deeming the expression legal, `regex` will then proceed to compile the expression into a NFA. It will pass through 3 stages:

1. the `syntax` module will first parse the expression into literal parts
2. the `syntax` module will then assemble the syntax tree from those parts and detect syntax errors in the process. The syntax trees are stored as tuples: `(id, args)`.
3. the `nfa` module will then construct the nfa that corresponds to the expression.

This finishes the initialization. After initialization the user will be able to pattern match by calling

```
re.match(text)
```
where `text` is the target string.