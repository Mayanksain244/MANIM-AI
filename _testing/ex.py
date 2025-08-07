from manim import *
import numpy as np

class TransformerArchitecture(Scene):
    def construct(self):
        # Title
        title = Text("Transformer Architecture", font_size=48, color=GOLD).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Input section
        self.show_input_section()
        self.wait(2)
        
        # Encoder section
        self.show_encoder_section()
        self.wait(2)
        
        # Multi-head attention detailed view
        self.show_attention_mechanism()
        self.wait(3)
        
        # Decoder section
        self.show_decoder_section()
        self.wait(2)
        
        # Final animation
        self.show_complete_flow()
        self.wait(3)

    def create_component_box(self, text, width=3, height=0.8, color=BLUE, text_size=20):
        """Create a styled component box with text"""
        box = RoundedRectangle(
            width=width, 
            height=height, 
            fill_color=color, 
            fill_opacity=0.3,
            stroke_color=color,
            stroke_width=2,
            corner_radius=0.1
        )
        text_obj = Text(text, font_size=text_size, color=WHITE)
        text_obj.move_to(box.get_center())
        return VGroup(box, text_obj)

    def show_input_section(self):
        """Show input processing components"""
        # Clear previous content except title
        self.clear_scene_except_title()
        
        # Input text
        input_text = Text("Input: 'The cat sat on the mat'", font_size=24, color=YELLOW)
        input_text.to_edge(LEFT).shift(UP * 2)
        self.play(Write(input_text))
        
        # Tokenization
        tokens = VGroup(*[
            Text(token, font_size=18, color=WHITE).set_background_stroke(color=BLUE, width=2)
            for token in ["The", "cat", "sat", "on", "the", "mat"]
        ]).arrange(RIGHT, buff=0.3).next_to(input_text, DOWN, buff=0.5)
        
        self.play(Create(tokens))
        
        # Input Embedding
        embedding_box = self.create_component_box("Input Embedding", width=4, color=BLUE)
        embedding_box.next_to(tokens, DOWN, buff=1)
        self.play(FadeIn(embedding_box))
        
        # Explanation
        embed_explanation = Text(
            "Converts tokens to dense vectors\n(e.g., 512 dimensions)", 
            font_size=16, 
            color=GRAY
        ).next_to(embedding_box, RIGHT, buff=0.5)
        self.play(Write(embed_explanation))
        
        # Positional Encoding
        pos_encoding_box = self.create_component_box("Positional Encoding", width=4, color=GREEN)
        pos_encoding_box.next_to(embedding_box, DOWN, buff=0.8)
        self.play(FadeIn(pos_encoding_box))
        
        # Positional encoding explanation
        pos_explanation = Text(
            "Adds position information\nsin/cos functions", 
            font_size=16, 
            color=GRAY
        ).next_to(pos_encoding_box, RIGHT, buff=0.5)
        self.play(Write(pos_explanation))
        
        # Addition symbol
        plus_symbol = Text("+", font_size=36, color=YELLOW)
        plus_symbol.move_to((embedding_box.get_center() + pos_encoding_box.get_center()) / 2)
        plus_symbol.shift(LEFT * 2)
        self.play(Write(plus_symbol))
        
        # Arrow to next stage
        arrow = Arrow(
            pos_encoding_box.get_bottom(),
            pos_encoding_box.get_bottom() + DOWN * 0.5,
            color=WHITE
        )
        self.play(GrowArrow(arrow))

    def show_encoder_section(self):
        """Show encoder components"""
        self.clear_scene_except_title()
        
        # Encoder title
        encoder_title = Text("Encoder Layer (N=6)", font_size=32, color=GOLD)
        encoder_title.shift(UP * 2.5)
        self.play(Write(encoder_title))
        
        # Multi-Head Attention
        attention_box = self.create_component_box("Multi-Head Attention", width=5, color=RED)
        attention_box.shift(UP * 1)
        self.play(FadeIn(attention_box))
        
        # Add & Norm 1
        add_norm1_box = self.create_component_box("Add & Norm", width=3, color=PURPLE)
        add_norm1_box.next_to(attention_box, DOWN, buff=0.5)
        self.play(FadeIn(add_norm1_box))
        
        # Feed Forward
        ff_box = self.create_component_box("Feed Forward Network", width=5, color=ORANGE)
        ff_box.next_to(add_norm1_box, DOWN, buff=0.5)
        self.play(FadeIn(ff_box))
        
        # Add & Norm 2
        add_norm2_box = self.create_component_box("Add & Norm", width=3, color=PURPLE)
        add_norm2_box.next_to(ff_box, DOWN, buff=0.5)
        self.play(FadeIn(add_norm2_box))
        
        # Residual connections
        self.show_residual_connections(attention_box, add_norm1_box, ff_box, add_norm2_box)
        
        # Explanations
        explanations = VGroup(
            Text("Self-attention mechanism", font_size=14, color=GRAY).next_to(attention_box, RIGHT, buff=0.5),
            Text("Residual + Layer Norm", font_size=14, color=GRAY).next_to(add_norm1_box, RIGHT, buff=0.5),
            Text("2-layer MLP with ReLU", font_size=14, color=GRAY).next_to(ff_box, RIGHT, buff=0.5),
            Text("Residual + Layer Norm", font_size=14, color=GRAY).next_to(add_norm2_box, RIGHT, buff=0.5)
        )
        self.play(*[Write(exp) for exp in explanations])

    def show_residual_connections(self, attention_box, add_norm1_box, ff_box, add_norm2_box):
        """Show residual connections"""
        # First residual connection
        residual1 = CurvedArrow(
            attention_box.get_left() + LEFT * 0.5,
            add_norm1_box.get_left() + LEFT * 0.5,
            color=YELLOW,
            stroke_width=2
        )
        self.play(Create(residual1))
        
        # Second residual connection
        residual2 = CurvedArrow(
            ff_box.get_left() + LEFT * 0.5,
            add_norm2_box.get_left() + LEFT * 0.5,
            color=YELLOW,
            stroke_width=2
        )
        self.play(Create(residual2))

    def show_attention_mechanism(self):
        """Show detailed multi-head attention"""
        self.clear_scene_except_title()
        
        # Attention title
        attention_title = Text("Multi-Head Attention Mechanism", font_size=32, color=GOLD)
        attention_title.shift(UP * 3)
        self.play(Write(attention_title))
        
        # Input representations
        input_vectors = VGroup()
        for i in range(3):
            vector = Rectangle(width=0.3, height=1.5, fill_color=BLUE, fill_opacity=0.7)
            vector.shift(LEFT * 4 + RIGHT * i * 0.5)
            input_vectors.add(vector)
        
        input_label = Text("Input\nVectors", font_size=16, color=WHITE)
        input_label.next_to(input_vectors, DOWN, buff=0.3)
        
        self.play(Create(input_vectors), Write(input_label))
        
        # Q, K, V transformations
        qkv_boxes = VGroup()
        colors = [RED, GREEN, BLUE]
        labels = ["Query (Q)", "Key (K)", "Value (V)"]
        
        for i, (color, label) in enumerate(zip(colors, labels)):
            box = self.create_component_box(label, width=2, height=1.2, color=color, text_size=16)
            box.shift(LEFT * 1 + RIGHT * i * 1.5 + UP * 1)
            qkv_boxes.add(box)
            
            # Arrows from input to QKV
            arrow = Arrow(
                input_vectors.get_top(),
                box.get_bottom(),
                color=color,
                stroke_width=2
            )
            self.play(GrowArrow(arrow))
        
        self.play(FadeIn(qkv_boxes))
        
        # QKV explanations
        qkv_explanations = VGroup(
            Text("What to look for", font_size=12, color=GRAY).next_to(qkv_boxes[0], DOWN, buff=0.2),
            Text("What to match", font_size=12, color=GRAY).next_to(qkv_boxes[1], DOWN, buff=0.2),
            Text("What to return", font_size=12, color=GRAY).next_to(qkv_boxes[2], DOWN, buff=0.2)
        )
        self.play(*[Write(exp) for exp in qkv_explanations])
        
        # Attention formula
        formula = MathTex(
            r"\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
            font_size=24,
            color=YELLOW
        )
        formula.shift(DOWN * 1.5)
        self.play(Write(formula))
        
        # Attention matrix visualization
        attention_matrix = self.create_attention_matrix()
        attention_matrix.next_to(formula, DOWN, buff=0.8)
        self.play(Create(attention_matrix))

    def create_attention_matrix(self):
        """Create attention matrix visualization"""
        # Create a 6x6 matrix to represent attention weights
        matrix = VGroup()
        
        for i in range(6):
            row = VGroup()
            for j in range(6):
                # Create attention weight (random for visualization)
                weight = np.random.random()
                opacity = weight * 0.8 + 0.2
                
                cell = Square(side_length=0.3, fill_opacity=opacity, fill_color=YELLOW)
                cell.shift(RIGHT * j * 0.3 + DOWN * i * 0.3)
                row.add(cell)
            matrix.add(row)
        
        # Add labels
        token_labels = ["The", "cat", "sat", "on", "the", "mat"]
        
        # Row labels (queries)
        for i, label in enumerate(token_labels):
            text = Text(label, font_size=10, color=WHITE)
            text.next_to(matrix[i][0], LEFT, buff=0.1)
            matrix.add(text)
        
        # Column labels (keys)
        for j, label in enumerate(token_labels):
            text = Text(label, font_size=10, color=WHITE)
            text.next_to(matrix[0][j], UP, buff=0.1)
            matrix.add(text)
        
        matrix_label = Text("Attention Weights", font_size=16, color=GRAY)
        matrix_label.next_to(matrix, DOWN, buff=0.3)
        matrix.add(matrix_label)
        
        return matrix

    def show_decoder_section(self):
        """Show decoder components"""
        self.clear_scene_except_title()
        
        decoder_title = Text("Decoder Layer (N=6)", font_size=32, color=GOLD)
        decoder_title.shift(UP * 2.5)
        self.play(Write(decoder_title))
        
        # Masked Multi-Head Attention
        masked_attention_box = self.create_component_box("Masked Multi-Head\nAttention", width=4, color=RED)
        masked_attention_box.shift(UP * 1.5)
        self.play(FadeIn(masked_attention_box))
        
        mask_explanation = Text("Prevents looking at future tokens", font_size=14, color=GRAY)
        mask_explanation.next_to(masked_attention_box, RIGHT, buff=0.5)
        self.play(Write(mask_explanation))
        
        # Add & Norm
        add_norm_box = self.create_component_box("Add & Norm", width=3, color=PURPLE)
        add_norm_box.next_to(masked_attention_box, DOWN, buff=0.5)
        self.play(FadeIn(add_norm_box))
        
        # Cross Attention
        cross_attention_box = self.create_component_box("Multi-Head\nCross-Attention", width=4, color=TEAL)
        cross_attention_box.next_to(add_norm_box, DOWN, buff=0.5)
        self.play(FadeIn(cross_attention_box))
        
        cross_explanation = Text("Attends to encoder output", font_size=14, color=GRAY)
        cross_explanation.next_to(cross_attention_box, RIGHT, buff=0.5)
        self.play(Write(cross_explanation))
        
        # Final components
        final_components = VGroup(
            self.create_component_box("Add & Norm", width=3, color=PURPLE),
            self.create_component_box("Feed Forward", width=4, color=ORANGE),
            self.create_component_box("Add & Norm", width=3, color=PURPLE),
            self.create_component_box("Linear & Softmax", width=4, color=GOLD)
        )
        
        # Position final components
        for i, component in enumerate(final_components):
            if i == 0:
                component.next_to(cross_attention_box, DOWN, buff=0.5)
            else:
                component.next_to(final_components[i-1], DOWN, buff=0.3)
        
        self.play(*[FadeIn(comp) for comp in final_components])
        
        # Output probability distribution
        output_text = Text("Output: Probability Distribution", font_size=18, color=YELLOW)
        output_text.next_to(final_components[-1], DOWN, buff=0.5)
        self.play(Write(output_text))

    def show_complete_flow(self):
        """Show complete transformer flow"""
        self.clear_scene_except_title()
        
        # Create simplified complete architecture
        components = [
            ("Input", BLUE),
            ("Embedding", BLUE),
            ("+ Pos Encoding", GREEN),
            ("Encoder × 6", RED),
            ("Decoder × 6", ORANGE),
            ("Output", GOLD)
        ]
        
        boxes = VGroup()
        for i, (text, color) in enumerate(components):
            box = self.create_component_box(text, width=3, color=color)
            if i == 0:
                box.shift(LEFT * 6 + UP * 1)
            else:
                box.next_to(boxes[i-1], RIGHT, buff=1)
            boxes.add(box)
        
        self.play(*[FadeIn(box) for box in boxes])
        
        # Add arrows between components
        arrows = VGroup()
        for i in range(len(boxes) - 1):
            arrow = Arrow(
                boxes[i].get_right(),
                boxes[i+1].get_left(),
                color=WHITE,
                stroke_width=2
            )
            arrows.add(arrow)
        
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        
        # Add data flow animation
        data_dot = Dot(color=YELLOW, radius=0.1)
        data_dot.move_to(boxes[0].get_center())
        self.play(Create(data_dot))
        
        for i in range(1, len(boxes)):
            self.play(
                data_dot.animate.move_to(boxes[i].get_center()),
                rate_func=smooth,
                run_time=0.8
            )
        
        # Final message
        final_text = Text(
            "Transformer: Attention Is All You Need!",
            font_size=24,
            color=GOLD
        )
        final_text.shift(DOWN * 2)
        self.play(Write(final_text))

    def clear_scene_except_title(self):
        """Clear all objects except the title"""
        objects_to_remove = [obj for obj in self.mobjects[1:]]  # Skip first object (title)
        if objects_to_remove:
            self.play(*[FadeOut(obj) for obj in objects_to_remove])

class TransformerFlow(Scene):
    """Additional scene showing information flow"""
    def construct(self):
        title = Text("Information Flow in Transformer", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create sentence
        sentence = "The cat sat"
        tokens = sentence.split()
        
        # Token visualization
        token_boxes = VGroup()
        for i, token in enumerate(tokens):
            box = RoundedRectangle(
                width=1.2, height=0.6,
                fill_color=BLUE, fill_opacity=0.3,
                stroke_color=BLUE
            )
            text = Text(token, font_size=18)
            token_viz = VGroup(box, text)
            token_viz.shift(LEFT * 3 + RIGHT * i * 1.5)
            token_boxes.add(token_viz)
        
        self.play(Create(token_boxes))
        
        # Show attention connections
        attention_lines = VGroup()
        for i in range(len(tokens)):
            for j in range(len(tokens)):
                if i != j:
                    line = Line(
                        token_boxes[i].get_center() + UP * 0.3,
                        token_boxes[j].get_center() + UP * 0.3,
                        color=YELLOW,
                        stroke_width=2,
                        stroke_opacity=0.6
                    )
                    attention_lines.add(line)
        
        self.play(Create(attention_lines))
        
        # Animate attention
        for line in attention_lines:
            self.play(line.animate.set_stroke(opacity=1), run_time=0.2)
            self.play(line.animate.set_stroke(opacity=0.3), run_time=0.2)
        
        self.wait(2)