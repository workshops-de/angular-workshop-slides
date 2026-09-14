
## Guard function

- Import the `CanDeactivateFn` interface from `@angular/router`
- Type the guard with the guarded component (`BookDetailPage`) and implement the fat arrow function

```ts
export const confirmLeaveGuardFn: CanDeactivateFn<BookDetailPage> = (route, state) => {
  // ...
};
```

```ts
return confirm('Do you really want to leave?');
```


Add guard to route:

```ts
{
  path: ...,
  component: ...,
  canDeactivate: [...]
}
```

