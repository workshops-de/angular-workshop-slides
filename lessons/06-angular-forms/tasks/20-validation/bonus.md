## Give your model an explicit type

Signal Forms infer the whole `form{:ts}`'s shape (and thus `schemaPath{:ts}` and `form.title{:ts}`, ...) from the type of your `model{:ts}` signal — no extra typing needed for the FormGroup itself. Still, giving the model an explicit interface can make the shape clearer to your teammates:

- Create an Interface `interface BookForm { ... }{:ts}` for your model's data.

---

- Type your `model{:ts}` signal explicitly: `signal<BookForm>({ ... }){:ts}`.
