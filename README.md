# Markov

The corpus was generated in the console, using:

```javascript
$('.team:not(.non-execs) .tooltip').each(function () { console.log($(this).text()) })
```

To install:

    pip install -r requirements.txt

And to run:

    python generate.py
