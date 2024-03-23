---
date_created: 2024-01-26
folder: quick_notes
date_modified: 2024-03-16
---
# Fast Facts related to Rust
``` toc
```

## Crates
## Variables
### `String` and `&str`
- `&str` 
	- string slice
	- reference to a string literal somewhere else
	- borrowed, immutable
	- static lifetime, borrows lifetime of referred string
- `String`
	- string literal
	- growable, mutable, owned
	- heap allocated
	- `Deref`, one of the many ways to turn into `&str` 
## Std functions
## Other

### Enums, Impls, and match
for some reason, match functions for enums work like this:
```rust
impl State {
    fn change_color(&mut self, color: (u8, u8, u8)) {
        self.color = color;
    }
    fn quit(&mut self) {
        self.quit = true;
    }
    fn echo(&mut self, s: String) {
        self.message = s
    }
    fn move_position(&mut self, p: Point) {
        self.position = p;
    }

    fn process(&mut self, message: Message) {
        // TODO: create a match expression to process the different message
        // variants
        // Remember: When passing a tuple as a function argument, you'll need
        // extra parentheses: fn function((t, u, p, l, e))
        match message {
            Message::Quit => self.quit(),
            Message::Move(point) => self.move_position(point),
            Message::Echo(m) => self.echo(m),
            Message::ChangeColor(r, g, b) => self.change_color((r, g, b)),
        }
    }
}
```

whats really important here is that in match, it kind of automatically guesses what the argument passed is
whats most likely gonna happen is that when a value type mismatch occurs an error is printed out
but rust compiler handles that for us, we just have to declare the match to map enums to actual function implementations
however this is a `State` implementation that makes use of enum mapping.
I am not really sure what is the practical use of this functionality but for now,