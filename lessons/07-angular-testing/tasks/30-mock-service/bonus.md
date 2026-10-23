## Spy on the real class instead

Sometimes you don't want a fully fake object. You only want to observe (or override) a single method and keep the rest of the class intact.

- **Spy before rendering** `BooksPage{:ts}` calls `getAll(){:ts}` in a field initializer, i.e. while the component is created. So the spy has to exist **before** `render(){:ts}`. Spy on the prototype and reuse your resource-shaped stub:

  ```ts
  const getAllSpy = vi.spyOn(BooksClient.prototype, 'getAll').mockReturnValue({
    value: () => [mobyDick, friends],
    isLoading: () => false,
    error: () => undefined
  } as unknown as ReturnType<BooksClient['getAll']>);
  ```

- **Render with the real `BooksClient{:ts}`** Don't replace the service this time. Provide what the real class needs instead: `await render(BooksPage, { providers: [provideHttpClient(), provideHttpClientTesting()] });{:ts}`.
- **Assert the call** `expect(getAllSpy).toHaveBeenCalledTimes(1);{:ts}` and check that both titles are rendered.
- **Clean up** A prototype spy outlives the test. Add `afterEach(() => vi.restoreAllMocks());{:ts}` so the next test gets the original `getAll(){:ts}` back.

> Why not `TestBed.inject(BooksClient){:ts}` first and spy on that instance? `render(){:ts}` configures the `TestBed{:ts}` itself. Once `inject(){:ts}` has created the test module, it can't be configured anymore, and the test fails.
