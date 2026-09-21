## Spy on a real instance instead

Sometimes you don't want a fully fake object, just to observe (or override) a single method while keeping the rest of the class intact.

- Get a real instance with `const booksClient = TestBed.inject(BooksClient);{:ts}` inside a `beforeEach{:ts}` that first configures a bare `TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] }){:ts}`.
- Replace the mock object with `const getAllSpy = vi.spyOn(booksClient, 'getAll').mockReturnValue(of([mobyDick, friends]));{:ts}`.
- Provide the same `booksClient{:ts}` instance to `render(){:ts}` via `providers: [{ provide: BooksClient, useValue: booksClient }]{:ts}`.
- Assert with `expect(getAllSpy).toHaveBeenCalledTimes(1);{:ts}`.
