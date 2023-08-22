from manim import *
import numpy as np


def streamlines(point):
    x, y = point[:2]
    return (x * RIGHT) + (y * UP)


def get_color_from_mag(mag):
    if mag > 50:
        return RED_D
    elif mag > 25:
        return ORANGE
    elif mag > 7.5:
        return GOLD_D
    elif mag > 2.5:
        return YELLOW_B
    else:
        return GREEN_B


def get_div_factor_from_mag(mag):
    if mag > 50:
        return 1.5
    elif mag > 25:
        return 1.65
    elif mag > 10:
        return 1.85
    elif mag > 5:
        return 2.2
    else:
        return 2.75


def normal(point, scale=False):
    x, y = point[:2]
    vec = np.array([x, y, 0])
    mag = np.linalg.norm(vec)
    col = get_color_from_mag(mag)
    div_factor = get_div_factor_from_mag(mag)
    if scale:
        vec = vec / (mag * div_factor)
    result = Vector(vec, color=col, tip_length=0.15).shift(point)
    return result


class Anim3b(Scene):
    def construct(self):
        func_tex = (Tex(r"$\vec{\bf{v}} = \vec{\bf{r}}$").to_edge(UL).add_background_rectangle(BLACK))
        plane = NumberPlane(x_range=[-7, 7, 1], y_range=[-4, 4, 1], x_length=14, y_length=8).add_coordinates()
        dots = VGroup(*[Dot(x * RIGHT + y * UP, radius=0.05)
                         for x in np.arange(-7.5, 7.5, 1)
                         for y in np.arange(-7.5, 7.5, 1)])

        field = VGroup(*[normal(x * RIGHT + y * UP)
                         for x in np.arange(-7.5, 7.5, 1)
                         for y in np.arange(-7.5, 7.5, 1)])

        stream = StreamLines(streamlines, x_range=[-7, 7, 0.2], y_range=[-7, 7, 0.2], padding=1)

        self.play(Create(plane, run_time=2.5))
        self.play(FadeIn(dots, run_time=1.5))
        self.play(ReplacementTransform(dots, field, run_time=1))
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.play(FadeIn(func_tex, run_time=1))
        self.wait(6)

# manim -pqh Anim3b.py Anim3b
