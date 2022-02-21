# AutoFilter client library

## Installation

In real conditions :

```
npm i '@ma-hackathon/auto-filter'
```

But since this package is not publish, use `npm install` and target the folder which containg the `package.json` of this lib (as explain in [official documentation](https://docs.npmjs.com/cli/v8/commands/npm-install)) :

```
npm i <path/to/this/lib>
```

## Usage

```ts
import Query, { And, Eq, Or } from '@ma-hackathon/auto-filter';

// Filter by color
Query().filter(Eq('color', 'red')).get(); // Eq(color, 'foo')

// Filter by color and size
// Option 1
Query().filter(And(Eq('color', 'red'), Eq('size', 'small'))).get() // And(Eq(color, 'red'), Eq(size, 'small'))
// Option 2
Query().filter(Eq('color', 'red')).and(Eq('size', 'small')).get()  // And(Eq(color, 'red'), Eq(size, 'small'))

// Filter on differents colors
// Option 1
Query().filter(Or(Eq('color', 'red'), Eq('color', 'green'))).get() // Or(Eq(color, 'red'), Eq(color, 'green'))
// Option 2
Query().filter(Eq('color', 'red')).or(Eq('color', 'green')).get() // Or(Eq(color, 'red'), Eq(color, 'green'))
```