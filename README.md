# Greek Celebrations in JSON Format

## Sample

```json
{
    "date": {
        "fixed": {
            "day": 23,
            "month": 4,
            "sunday": false
        },
        "easter": 1,
    },
    "celebrations": {
        "names": [
            "ΓΙΩΡΓΟΣ",
            "ΓΕΩΡΓΙΟΣ",
            "ΓΕΩΡΓΙΑ"
        ],
        "holidays": [
            "Αγίου Γεωργίου"
        ]
    }
}
```

## Explanation

- `date`: Represents the date of the event, can be `fixed`, `easter` or both
    - `fixed`: Represents a fixed date
        - `day`: day of the month
        - `month`: month (1 is January, 12 is December)
        - `sunday`: if this field is set to `true`, the date is shifted to the succeeding Sunday if the current day is not Sunday; if this field is missing it is considered `false`
    - `easter`: Represents a date relative to the Orthodox Easter, can be positive or negative
    - At least one of `fixed` or `easter` must be set; if both are present, the event takes place in the latest date of the two, `max(fixed, easter)`
- `celebrations`: The celebrations, contains subarrays `names` and `holidays`
    - `names`: Name days
    - `holidays`: National holidays

## Notes

There can exist duplicate dates inside the array, for example:

```json
{
    "date": { "fixed": { "day": 1, "month": 1 } },
    "celebrations": {
        "names": [ "ΓΙΩΡΓΟΣ", "ΓΕΩΡΓΙΟΣ", "ΓΕΩΡΓΙΑ" ]
    }
},
{
    "date": { "fixed": { "day": 1, "month": 1 } },
    "celebrations": {
        "holidays": [ "Αγίου Γεωργίου" ]
    }
}
```

In this case all stated holidays and name days are valid.
