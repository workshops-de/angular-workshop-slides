## Give your model an explicit type

Signal Forms infer the whole `form`'s shape (and thus `schemaPath` and `form.title`, ...) from the type of your `model` signal — no extra typing needed for the FormGroup itself. Still, giving the model an explicit interface can make the shape clearer to your teammates:

- Create an Interface `interface BookForm { ... }` for your model's data.
- Type your `model` signal explicitly: `signal<BookForm>({ ... })`.
