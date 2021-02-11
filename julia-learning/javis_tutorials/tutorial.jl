using Javis, Animations
myvideo = Video(500, 500)

function ground(args...)
    background("white") 
    sethue("black")
end

function object(p=O, color="black")
    sethue(color)
    circle(p, 25, :fill)
    return p
end
##
Background(1:70, ground)
red_ball = Object(1:70, (args...) -> object(O, "red"), Point(100, 0))

render(
    myvideo;
    pathname="circle.gif"
)
##
Background(1:70, ground)
red_ball = Object(1:70, (args...) -> object(O, "red"), Point(100,0))
blue_ball = Object(1:70, (args...) -> object(O, "blue"), Point(200,80))

render(
    myvideo;
    pathname="circle.gif"
)
##
Background(1:70, ground)
red_ball = Object(1:70, (args...)->object(O, "red"), Point(100,0))
act!(red_ball, Action(anim_rotate_around(2π, O)))
render(
    myvideo;
    pathname="round.gif"
)
##
Background(1:70, ground)
red_ball = Object(1:70, (args...)->object(O, "red"), Point(100,0))
act!(red_ball, Action(anim_rotate_around(2π, O)))
blue_ball = Object(1:70, (args...)-> object(O, "blue"), Point(200,80))
act!(blue_ball, Action(anim_rotate_around(2π, 0.0, red_ball)))
render(
    myvideo;
    ffmpeg_loglevel = "debug",
    pathname="round2.gif"
)
##