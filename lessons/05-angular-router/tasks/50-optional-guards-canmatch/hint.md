```ts
@Injectable({
  providedIn: 'root'
})
export class UserState {
  isLoggedIn = true;
}
```

```ts
const service = inject(UserState);
```

```ts
{
  path: 'books',
  //...
  canMatch: [
  //...
  ]
}
```
