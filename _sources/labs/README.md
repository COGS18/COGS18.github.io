# CodingLabs

This private repository is for developing coding labs.

CodingLabs are hosted to view and download on the course website [here](https://cogs18.github.io/CodingLabs/).

It follows the structure for `nbgrader`, for building and grading assignments.

This repository requires `nbgrader` >= 0.5.0.

`nbgrader`: https://nbgrader.readthedocs.io/en/stable/

Directory Structure:
- `source`: Where to create master version of the assignments, written with the answers included.
- `release`: The release version of the assignment (answers removed), automatically generated from source.
- `submitted`: Submitted assignments from the students.
- `autograded`: Graded assignments, automatically graded by nbgrader.

^ The 'submitted', 'release', and 'autograded' folders are not included in this repository (they will be large to sync, and offer no benefit to being hosted), when using datahub.


`Archive` : materials used in previous quarters:

- `_Su20` : indicates materials for a 5-week summer course, rather than the typical 10 week quarter
- `CL6*` : includes Coding Lab where inheritance and date/datetime were the focus
- CL7*withtests : for when testing has been covered prior to CL7
- *cravings : student example for CL7
- CL8 & CL10 : from when I would release "instructions for project-centric coding labs"
