## Preventing the default link behaviour

```ts
handleDetailClick(click: MouseEvent) {
  click.preventDefault();

  console.log('Click Details-Link:', click);
}
```
