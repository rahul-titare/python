Fractal Tree using python and matplotlib

This python code builds a beautiful Fractal Tree

1. It first draws a line in middle with height (ht)
2. At endpoint of previous line, it draws another two lines rotated at an angle theta and -theta
3. This goes in recursion. Every time a new recursion call is made 
	a. height reduces by (height_reduction) factor
	b. line width reduces by (width_reduction) factor
4. Recursion breaks where height goes below min_height
