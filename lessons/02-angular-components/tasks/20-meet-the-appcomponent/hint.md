## npm start

If you are not familiar with `npm` here is what `npm start --  --open` does.
You will find a file called `package.json` in your Angular project.
If you have a look into the file you will find a section called `scripts`.
There you can see that the script `start` executes the Angular CLI command `ng serve`.
That means `npm start` executes `ng serve`.

If you want to pass additional arguments to `ng serve` you can to that with npm to.
By writing `--` you pass the following arguments to `ng serve`.
That means `ng serve --open` is equivilant to `npm start -- --open`.

The argument `--open` opens the default browser after the compilation of your Angular project has been completed.
