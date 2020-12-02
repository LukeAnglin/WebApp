---
title: JavaScript Intro 
author: Luke Anglin
image: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
description: Introduction to Javascript.  Some knowledge is needed in order to write this Flask application better!
topics: Testing, RegEx, syntax, and other things that I think I'd forget otherwise!
---

# Testing

## Kinds of Tests

<!-- Image pyramid -->
<img src="https://javascriptwebscrapingguy.com/wp-content/uploads/2019/05/Pyramid-of-Tests.jpg" alt="pyramid of tests" width = "400" height = "400">

<!-- Testing Descriptions -->
<dl>
    <dt>Unit Testing</dt>
    <dd>Blocks of code, single functions</dd>
    <dt>Integration Testing</dt>
    <dd>Dependencies, functions calling functions</dd>
    <dt>End to End (E2E) or Acceptance Testing</dt>
    <dd>Throw the kid in the pool and see if he swims - Browser Testing</dd>
</dl>

## Frameworks

### Jest

Designed by facebook.  Aims for a "zero-configuration" experience.

```bash
npm install --save-dev jest
```


# Var, Let, and Const


# JS Regex

<!-- Tomorrow fix example too big and fix issue with code blocks embedded -->


For a comprehensive guide, see the [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)

## Constructor

```js
// Patterns and modifiers may be strings
// Modifiers include: g, i and m
new RegExp('Example: ([\w\W]*)\n([\w\W]*)\nEND Example', 'g')
```

## Replacements






