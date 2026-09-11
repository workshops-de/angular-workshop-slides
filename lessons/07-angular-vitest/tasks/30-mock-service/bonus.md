## Spy on a real instance instead

Sometimes you don't want a fully fake object, just to observe (or override) a single method while keeping the rest of the class intact.

- Get a real instance with `const booksClient = TestBed.inject(BooksClient);` inside a `beforeEach` that first configures a bare `TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] })`.
- Replace the mock object with `const getAllSpy = vi.spyOn(booksClient, 'getAll').mockReturnValue(of([mobyDick, friends]));`.
- Provide the same `booksClient` instance to `render()` via `providers: [{ provide: BooksClient, useValue: booksClient }]`.
- Assert with `expect(getAllSpy).toHaveBeenCalledTimes(1);`.
