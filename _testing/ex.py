# from manim import *
# from manim.utils.color import Colors

# class DecisionTreeAnimation(Scene):
#     def construct(self):
#         # Title
#         title = Text("Decision Tree Example: Play Tennis?", font_size=36)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(title.animate.to_edge(UP))
#         self.wait(0.5)

#         # Dataset explanation
#         data_text = Text("Based on weather conditions:", font_size=24)
#         data_text.next_to(title, DOWN, buff=0.5)
        
#         data_table = MathTable(
#             [["Outlook", "Humidity", "Wind", "Play Tennis?"],
#              ["Sunny", "High", "Weak", "No"],
#              ["Sunny", "High", "Strong", "No"],
#              ["Overcast", "High", "Weak", "Yes"],
#              ["Rain", "High", "Weak", "Yes"],
#              ["Rain", "Normal", "Weak", "Yes"],
#              ["Rain", "Normal", "Strong", "No"],
#              ["Overcast", "Normal", "Strong", "Yes"],
#              ["Sunny", "High", "Weak", "No"],
#              ["Sunny", "Normal", "Weak", "Yes"],
#              ["Rain", "Normal", "Weak", "Yes"],
#              ["Sunny", "Normal", "Strong", "Yes"],
#              ["Overcast", "High", "Strong", "Yes"],
#              ["Rain", "High", "Strong", "No"]],
#             include_outer_lines=True)
        
#         data_table.scale(0.4)
#         data_table.next_to(data_text, DOWN, buff=0.5)
        
#         self.play(Write(data_text))
#         self.wait(0.5)
#         self.play(Create(data_table))
#         self.wait(2)
        
#         # Clear the screen for tree animation
#         self.play(
#             FadeOut(title),
#             FadeOut(data_text),
#             FadeOut(data_table)
#         )
#         self.wait(0.5)
        
#         # Decision tree construction
#         root = self.create_node("Outlook?", radius=0.5)
#         root.move_to(UP * 2)
        
#         # Level 1 branches
#         sunny = self.create_node("Sunny", radius=0.4, color=YELLOW)
#         sunny.move_to(root.get_center() + DOWN * 1.5 + LEFT * 3)
        
#         overcast = self.create_node("Overcast", radius=0.4, color=BLUE)
#         overcast.move_to(root.get_center() + DOWN * 1.5)
        
#         rain = self.create_node("Rain", radius=0.4, color=GREEN)
#         rain.move_to(root.get_center() + DOWN * 1.5 + RIGHT * 3)
        
#         # Animate root and first level
#         self.play(GrowFromCenter(root))
#         self.wait(0.5)
        
#         # Draw branches to first level
#         self.play(
#             Create(self.create_arrow(root, sunny)),
#             Create(self.create_arrow(root, overcast)),
#             Create(self.create_arrow(root, rain)),
#             run_time=1.5
#         )
        
#         self.play(
#             GrowFromCenter(sunny),
#             GrowFromCenter(overcast),
#             GrowFromCenter(rain),
#             run_time=1.5
#         )
#         self.wait(1)
        
#         # Level 2 - Sunny branch
#         sunny_humidity = self.create_node("Humidity?", radius=0.5)
#         sunny_humidity.move_to(sunny.get_center() + DOWN * 1.5)
        
#         self.play(
#             Create(self.create_arrow(sunny, sunny_humidity)),
#             run_time=1
#         )
#         self.play(GrowFromCenter(sunny_humidity))
#         self.wait(0.5)
        
#         # Level 3 under Sunny -> Humidity
#         sunny_high = self.create_node("No", radius=0.4, color=RED)
#         sunny_high.move_to(sunny_humidity.get_center() + DOWN * 1.5 + LEFT * 1.5)
        
#         sunny_normal = self.create_node("Yes", radius=0.4, color=GREEN)
#         sunny_normal.move_to(sunny_humidity.get_center() + DOWN * 1.5 + RIGHT * 1.5)
        
#         self.play(
#             Create(self.create_arrow(sunny_humidity, sunny_high)),
#             Create(self.create_arrow(sunny_humidity, sunny_normal)),
#             run_time=1.5
#         )
        
#         self.play(
#             GrowFromCenter(sunny_high),
#             GrowFromCenter(sunny_normal),
#             run_time=1.5
#         )
#         self.wait(1)
        
#         # Level 2 - Overcast branch (direct result)
#         overcast_leaf = self.create_node("Yes", radius=0.4, color=GREEN)
#         overcast_leaf.move_to(overcast.get_center() + DOWN * 1.5)
        
#         self.play(
#             Create(self.create_arrow(overcast, overcast_leaf)),
#             run_time=1
#         )
#         self.play(GrowFromCenter(overcast_leaf))
#         self.wait(0.5)
        
#         # Level 2 - Rain branch
#         rain_wind = self.create_node("Wind?", radius=0.5)
#         rain_wind.move_to(rain.get_center() + DOWN * 1.5)
        
#         self.play(
#             Create(self.create_arrow(rain, rain_wind)),
#             run_time=1
#         )
#         self.play(GrowFromCenter(rain_wind))
#         self.wait(0.5)
        
#         # Level 3 under Rain -> Wind
#         rain_weak = self.create_node("Yes", radius=0.4, color=GREEN)
#         rain_weak.move_to(rain_wind.get_center() + DOWN * 1.5 + LEFT * 1.5)
        
#         rain_strong = self.create_node("No", radius=0.4, color=RED)
#         rain_strong.move_to(rain_wind.get_center() + DOWN * 1.5 + RIGHT * 1.5)
        
#         self.play(
#             Create(self.create_arrow(rain_wind, rain_weak)),
#             Create(self.create_arrow(rain_wind, rain_strong)),
#             run_time=1.5
#         )
        
#         self.play(
#             GrowFromCenter(rain_weak),
#             GrowFromCenter(rain_strong),
#             run_time=1.5
#         )
#         self.wait(2)
        
#         # Highlight the complete tree
#         self.play(
#             *[Flash(node, flash_radius=0.7, color=node.color) 
#               for node in [root, sunny, overcast, rain, sunny_humidity, 
#                           sunny_high, sunny_normal, overcast_leaf, 
#                           rain_wind, rain_weak, rain_strong]],
#             run_time=2
#         )
#         self.wait(3)
        
#     def create_node(self, text, radius=0.5, color=WHITE):
#         """Create a circular node with text"""
#         circle = Circle(radius=radius, color=color)
#         label = Text(text, font_size=20, color=color)
#         label.move_to(circle.get_center())
#         return VGroup(circle, label)
    
#     def create_arrow(self, start_node, end_node, buff=0.1):
#         """Create an arrow between two nodes"""
#         start_point = start_node[0].get_bottom()
#         end_point = end_node[0].get_top()
#         return Arrow(start_point, end_point, buff=buff, color=GREY)
from manim import *

class ArchitectureDiagram(Scene):
    def construct(self):
        # 1. Define Styles
        box_config = {"color": BLUE, "fill_opacity": 0.2, "stroke_width": 2}
        text_scale = 0.6

        # 2. Create Nodes (Boxes & Text)
        # Central Controller
        controller = Rectangle(width=3.5, height=1.5, **box_config)
        controller_txt = Text("Controller\n(main.py)", font_size=24).move_to(controller)
        controller_group = VGroup(controller, controller_txt)

        # User Input (Left)
        user_input = Rectangle(width=2.5, height=1.2, **box_config)
        user_input.move_to(LEFT * 5)
        user_input_txt = Text("User Input", font_size=24).move_to(user_input)
        user_input_group = VGroup(user_input, user_input_txt)

        # Groq LLM (Top)
        groq = Rectangle(width=3, height=1.2, **box_config)
        groq.move_to(UP * 2.5)
        groq_txt = Text("Groq LLM\n(Generator)", font_size=24).move_to(groq)
        groq_group = VGroup(groq, groq_txt)

        # Verifier & Fixer (Bottom)
        verifier = Rectangle(width=3, height=1.2, **box_config)
        verifier.move_to(DOWN * 2.5)
        verifier_txt = Text("Verifier & Fixer", font_size=24).move_to(verifier)
        verifier_group = VGroup(verifier, verifier_txt)

        # Manim Executor (Right)
        executor = Rectangle(width=2.5, height=1.2, **box_config)
        executor.move_to(RIGHT * 3.5)
        executor_txt = Text("Executor", font_size=24).move_to(executor)
        executor_group = VGroup(executor, executor_txt)

        # Video Output (Far Right)
        video = Rectangle(width=2, height=1.2, color=GREEN, fill_opacity=0.2)
        video.move_to(RIGHT * 6)
        video_txt = Text("MP4", font_size=24).move_to(video)
        video_group = VGroup(video, video_txt)

        # 3. Create Arrows
        # Use 'buff=0' to touch the boxes, or small value for gap
        arr_input_main = Arrow(user_input.get_right(), controller.get_left(), buff=0.1)
        
        # Two-way arrows for Groq and Verifier (curved for style)
        arr_main_groq = Arrow(controller.get_top(), groq.get_bottom(), buff=0.1)
        arr_groq_main = Arrow(groq.get_bottom(), controller.get_top(), buff=0.1).shift(RIGHT*0.2)
        arr_main_groq.shift(LEFT*0.2) # Offset to show two distinct paths if desired, or keep simple
        
        # Simple straight arrows usually look cleaner for flowcharts
        arrow_up = Arrow(controller.get_top(), groq.get_bottom(), buff=0.1)
        arrow_down = Arrow(groq.get_bottom(), controller.get_top(), buff=0.1)
        
        arrow_to_ver = Arrow(controller.get_bottom(), verifier.get_top(), buff=0.1, color=RED)
        arrow_from_ver = Arrow(verifier.get_top(), controller.get_bottom(), buff=0.1, color=GREEN)
        # Offset them slightly to see the loop
        arrow_to_ver.shift(LEFT * 0.3)
        arrow_from_ver.shift(RIGHT * 0.3)

        arr_main_exec = Arrow(controller.get_right(), executor.get_left(), buff=0.1)
        arr_exec_vid = Arrow(executor.get_right(), video.get_left(), buff=0.1)

        # 4. Animation Sequence
        # Phase 1: Input
        self.play(FadeIn(user_input_group))
        self.play(GrowArrow(arr_input_main))
        self.play(FadeIn(controller_group))
        
        # Phase 2: Generation Loop
        self.play(GrowArrow(arrow_up))
        self.play(FadeIn(groq_group))
        self.play(Indicate(groq_group, color=PURPLE))
        self.play(GrowArrow(arrow_down)) # Return code
        
        # Phase 3: Verification Loop
        self.play(GrowArrow(arrow_to_ver))
        self.play(FadeIn(verifier_group))
        self.play(Indicate(verifier_group, color=RED)) # Simulating check
        self.play(GrowArrow(arrow_from_ver)) # Return fixed code
        
        # Phase 4: Execution
        self.play(GrowArrow(arr_main_exec))
        self.play(FadeIn(executor_group))
        self.play(GrowArrow(arr_exec_vid))
        self.play(FadeIn(video_group))
        self.play(Indicate(video_group, scale_factor=1.2, color=GREEN))

        self.wait(2)