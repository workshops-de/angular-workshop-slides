<details>
<summary>Create the user state</summary>

```ts
@Injectable({
  providedIn: 'root'
})
export class UserState {
  isLoggedIn = true;
}
```

</details>

<details>
<summary>Create a `canMatch{:ts}`-Guard</summary>

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

</details>
