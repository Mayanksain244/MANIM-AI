SYSTEM_PROMPT = """You are an expert Python programmer specializing in the Manim animation library. 
Generate complete, executable Manim code based on the user's description. Follow these rules:

1. Always start with `from manim import *`
2. Create a class that inherits from `Scene`
3. Include all necessary imports
4. Use proper Manim syntax and best practices
5. Keep animations simple and clear
6. Add comments explaining key parts
7. Return ONLY the code, no additional explanation

NO PREAMBLE
do not add ''' python or ''' either at the start or end
"""

FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": "Display a solid red square on the left and a solid blue circle overlapping it from the top right. On the right side of the screen, show a green shape representing the union—combining the full areas of both the square and the circle into a single merged shape."
    },
    {
        "role": "assistant",
        "content": """from manim import *

class UnionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Union(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0.3, 0])
        self.add(sq, cr, un)"""
    },
    {
        "role": "user",
        "content": "Display a thick parametric sine curve and a version of the same curve shifted upward, with its color smoothly transitioning from blue to red along its length. The gradient visually emphasizes the direction and flow of the curve."
    },
    {
        "role": "assistant",
        "content": """from manim import *

class LineGradientExample(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)"""
    },
    {
        "role": "user",
        "content": "Display a 2×2 table with row and column labels. The row heading text is colored red-blue gradient, the first column’s text is colored green, others are white, making each section visually distinct."
    },
    {
        "role": "assistant",
        "content": """from manim import *

class SetColumnColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(table)"""
    },
    {
        "role": "user",
        "content": "Display the text “Alice and Bob” in large font on the screen, then animate it being erased in reverse, as if unwriting it."
    },
    {
        "role": "assistant",
        "content": """from manim import *

class UnwriteReverseTrue(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text))"""
    },
    {
        "role": "user",
        "content": "Display a five-pointed star (pentagram) with evenly spaced points, sized with a radius of 2 units. The star is centered on the screen and shown with default styling."
    },
    {
        "role": "assistant",
        "content": """from manim import *

class RegularPolygramExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        self.add(pentagram)"""
    },
    {
        "role": "user",
        "content": "Display a square by fading it in. Then, rotate the square 45 degrees. Finally, fade the square out and pause for one second."
    },
    {
        "role": "assistant",
        "content": """from manim import *

class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)"""
    },
    {
        "role": "user",
        "content": """Display three large rectangles vertically aligned on the left side of the screen. After they fade in, each rectangle transforms into a small filled circle on the right side using different fade styles:

- The top rectangle stretches as it fades into the circle.
- The middle rectangle fades into the circle without stretching and without dimming to match the target.
- The bottom rectangle fades into the circle without stretching but dims to match the target's brightness.

Finally, all objects fade out together."""
    },
    {
        "role": "assistant",
        "content": """from manim import *

class DifferentFadeTransforms(Scene):
    def construct(self):
        starts = [Rectangle(width=4, height=1) for _ in range(3)]
        VGroup(*starts).arrange(DOWN, buff=1).shift(3*LEFT)
        targets = [Circle(fill_opacity=1).scale(0.25) for _ in range(3)]
        VGroup(*targets).arrange(DOWN, buff=1).shift(3*RIGHT)

        self.play(*[FadeIn(s) for s in starts])
        self.play(
            FadeTransform(starts[0], targets[0], stretch=True),
            FadeTransform(starts[1], targets[1], stretch=False, dim_to_match=0),
            FadeTransform(starts[2], targets[2], stretch=False, dim_to_match=1)
        )

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])"""
    }]