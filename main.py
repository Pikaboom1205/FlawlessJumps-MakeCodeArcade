enum ActionKind {
    Walking,
    Idle,
    Jumping
}
namespace SpriteKind {
    export const STAR = SpriteKind.create()
    export const COIN = SpriteKind.create()
    export const LAVA = SpriteKind.create()
    export const LAVATWO = SpriteKind.create()
    export const TREASURECHEST = SpriteKind.create()
    export const TREASURECHEST2 = SpriteKind.create()
    export const SEAWEEDTHREE = SpriteKind.create()
    export const SEA1 = SpriteKind.create()
    export const SEA2 = SpriteKind.create()
    export const SEAWEEDTWO = SpriteKind.create()
    export const SAND = SpriteKind.create()
    export const SEAWEED1 = SpriteKind.create()
    export const SAND2 = SpriteKind.create()
    export const DUCKY = SpriteKind.create()
    export const SLEEPYRUBBERDUCKY = SpriteKind.create()
    export const GOOMBA = SpriteKind.create()
    export const BAT = SpriteKind.create()
    export const CHECKPOINT = SpriteKind.create()
}
info.onScore(3000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SEAWEEDTHREE, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1000)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SEA2, function (sprite8, otherSprite8) {
    info.changeLifeBy(-1000)
})
info.onScore(1000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.COIN, function (sprite7, otherSprite7) {
    info.changeScoreBy(10)
    sprites.destroy(otherSprite7, effects.fountain, 100)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SAND, function (sprite4, otherSprite4) {
    info.changeLifeBy(-1000)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.setVolume(255)
    THEPLATFORMER.vy = -110
    if (THEPLATFORMER.isHittingTile(CollisionDirection.Bottom)) {
        THEPLATFORMER.startEffect(effects.rings, 350)
        music.play(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        THEPLATFORMER.vy = -110
        JUMP = true
    } else if (JUMP == true) {
        THEPLATFORMER.startEffect(effects.rings, 350)
        music.play(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        THEPLATFORMER.vy = -110
        JUMP = false
        scene.cameraShake(2, 100)
    }
    if (THEPLATFORMER.vy == 0) {
        THEPLATFORMER.vy = 110
        if (controller.left.isPressed()) {
            animation.runImageAnimation(
            THEPLATFORMER,
            [img`
                . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f b e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d e e e e e f . . . 
                . . . f e 4 e d d 4 f . . . . . 
                . . . f 2 2 e d d e f . . . . . 
                . . f f 5 5 f e e f f f . . . . 
                . . f f f f f f f f f f . . . . 
                . . . f f f . . . f f . . . . . 
                `,img`
                . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f b e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e e f f . . . . 
                . . . f 2 2 2 e d d 4 . . . . . 
                . . . f 2 2 2 e d d e . . . . . 
                . . . f 5 5 4 f e e f . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . . . . f f f . . . . . . . 
                `,img`
                . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f b e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e d d 4 . . . . 
                . . . f 2 2 2 2 e d d e . . . . 
                . . f f 5 5 4 4 f e e f . . . . 
                . . f f f f f f f f f f . . . . 
                . . . f f f . . . f f . . . . . 
                `],
            280,
            true
            )
        }
        if (controller.right.isPressed()) {
            animation.runImageAnimation(
            THEPLATFORMER,
            [img`
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e e e d d d f . . . 
                . . . . . f 4 d d e 4 e f . . . 
                . . . . . f e d d e 2 2 f . . . 
                . . . . f f f e e f 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . . 
                `,img`
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 2 2 2 f . . . 
                . . . . . e d d e 2 2 2 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . . 
                `,img`
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . 4 d d e 4 4 4 e f . . . 
                . . . . e d d e 2 2 2 2 f . . . 
                . . . . f e e f 4 4 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . . 
                `],
            280,
            true
            )
        }
    }
    animation.stopAnimation(animation.AnimationTypes.All, THEPLATFORMER)
})
info.onScore(9000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.TREASURECHEST, function (sprite, otherSprite) {
    animation.runImageAnimation(
    THETREASURECHEST,
    [img`
        . . b b b b b b b b b b b b . . 
        . b e 4 4 4 4 4 4 4 4 4 4 e b . 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e e 4 4 4 4 4 4 4 4 4 4 e e b 
        b e e e e e e e e e e e e e e b 
        b e e e e e e e e e e e e e e b 
        b b b b b b b d d b b b b b b b 
        c b b b b b b c c b b b b b b c 
        c c c c c c b c c b c c c c c c 
        b e e e e e c b b c e e e e e b 
        b e e e e e e e e e e e e e e b 
        b c e e e e e e e e e e e e c b 
        b b b b b b b b b b b b b b b b 
        . b b . . . . . . . . . . b b . 
        `,img`
        . b b b b b b b b b b b b b b . 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e e 4 4 4 4 4 4 4 4 4 4 e e b 
        b b b b b b b d d b b b b b b b 
        . b b b b b b c c b b b b b b . 
        b c c c c c b c c b c c c c c b 
        b c c c c c c b b c c c c c c b 
        b c c c c c c c c c c c c c c b 
        b c c c c c c c c c c c c c c b 
        b b b b b b b b b b b b b b b b 
        b e e e e e e e e e e e e e e b 
        b e e e e e e e e e e e e e e b 
        b c e e e e e e e e e e e e c b 
        b b b b b b b b b b b b b b b b 
        . b b . . . . . . . . . . b b . 
        `],
    1000,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    THEPLATFORMER,
    [img`
        . . . . . . . . . . . . . . . . 
        . . . . f f f f f f . . . . . . 
        . . . f 2 f e e e e f f . . . . 
        . . f 2 2 2 f e e e e f f . . . 
        . . f e e e e f f e e e f . . . 
        . f e 2 2 2 2 e e f f f f . . . 
        . f 2 e f f f f 2 2 2 e f . . . 
        . f f f e e e f f f f f f f . . 
        . f e e 4 4 f b e 4 4 e f f . . 
        . . f e d d f 1 4 d 4 e e f . . 
        . . . f d d d e e e e e f . . . 
        . . . f e 4 e d d 4 f . . . . . 
        . . . f 2 2 e d d e f . . . . . 
        . . f f 5 5 f e e f f f . . . . 
        . . f f f f f f f f f f . . . . 
        . . . f f f . . . f f . . . . . 
        `,img`
        . . . . f f f f f f . . . . . . 
        . . . f 2 f e e e e f f . . . . 
        . . f 2 2 2 f e e e e f f . . . 
        . . f e e e e f f e e e f . . . 
        . f e 2 2 2 2 e e f f f f . . . 
        . f 2 e f f f f 2 2 2 e f . . . 
        . f f f e e e f f f f f f f . . 
        . f e e 4 4 f b e 4 4 e f f . . 
        . . f e d d f 1 4 d 4 e e f . . 
        . . . f d d d d 4 e e e f . . . 
        . . . f e 4 4 4 e e f f . . . . 
        . . . f 2 2 2 e d d 4 . . . . . 
        . . . f 2 2 2 e d d e . . . . . 
        . . . f 5 5 4 f e e f . . . . . 
        . . . . f f f f f f . . . . . . 
        . . . . . . f f f . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . . 
        . . . . f f f f f f . . . . . . 
        . . . f 2 f e e e e f f . . . . 
        . . f 2 2 2 f e e e e f f . . . 
        . . f e e e e f f e e e f . . . 
        . f e 2 2 2 2 e e f f f f . . . 
        . f 2 e f f f f 2 2 2 e f . . . 
        . f f f e e e f f f f f f f . . 
        . f e e 4 4 f b e 4 4 e f f . . 
        . . f e d d f 1 4 d 4 e e f . . 
        . . . f d d d e e e e e f . . . 
        . . . f e 4 e d d 4 f . . . . . 
        . . . f 2 2 e d d e f . . . . . 
        . . f f 5 5 f e e f f f . . . . 
        . . f f f f f f f f f f . . . . 
        . . . f f f . . . f f . . . . . 
        `,img`
        . . . . f f f f f f . . . . . . 
        . . . f 2 f e e e e f f . . . . 
        . . f 2 2 2 f e e e e f f . . . 
        . . f e e e e f f e e e f . . . 
        . f e 2 2 2 2 e e f f f f . . . 
        . f 2 e f f f f 2 2 2 e f . . . 
        . f f f e e e f f f f f f f . . 
        . f e e 4 4 f b e 4 4 e f f . . 
        . . f e d d f 1 4 d 4 e e f . . 
        . . . f d d d d 4 e e e f . . . 
        . . . f e 4 4 4 e e f f . . . . 
        . . . f 2 2 2 e d d 4 . . . . . 
        . . . f 2 2 2 e d d e . . . . . 
        . . . f 5 5 4 f e e f . . . . . 
        . . . . f f f f f f . . . . . . 
        . . . . . . f f f . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . . 
        . . . . f f f f f f . . . . . . 
        . . . f 2 f e e e e f f . . . . 
        . . f 2 2 2 f e e e e f f . . . 
        . . f e e e e f f e e e f . . . 
        . f e 2 2 2 2 e e f f f f . . . 
        . f 2 e f f f f 2 2 2 e f . . . 
        . f f f e e e f f f f f f f . . 
        . f e e 4 4 f b e 4 4 e f f . . 
        . . f e d d f 1 4 d 4 e e f . . 
        . . . f d d d d 4 e e e f . . . 
        . . . f e 4 4 4 e d d 4 . . . . 
        . . . f 2 2 2 2 e d d e . . . . 
        . . f f 5 5 4 4 f e e f . . . . 
        . . f f f f f f f f f f . . . . 
        . . . f f f . . . f f . . . . . 
        `],
    280,
    false
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SAND2, function (sprite6, otherSprite6) {
    info.changeLifeBy(-1000)
})
info.onScore(6000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SEA1, function (sprite5, otherSprite5) {
    info.changeLifeBy(-1000)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    THEPLATFORMER,
    [img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f . . . . 
        . . . . f f e e e e f 2 f . . . 
        . . . f f e e e e f 2 2 2 f . . 
        . . . f e e e f f e e e e f . . 
        . . . f f f f e e 2 2 2 2 e f . 
        . . . f e 2 2 2 f f f f e 2 f . 
        . . f f f f f f f e e e f f f . 
        . . f f e 4 4 e b f 4 4 e e f . 
        . . f e e 4 d 4 1 f d d e f . . 
        . . . f e e e e e d d d f . . . 
        . . . . . f 4 d d e 4 e f . . . 
        . . . . . f e d d e 2 2 f . . . 
        . . . . f f f e e f 5 5 f f . . 
        . . . . f f f f f f f f f f . . 
        . . . . . f f . . . f f f . . . 
        `,img`
        . . . . . . f f f f f f . . . . 
        . . . . f f e e e e f 2 f . . . 
        . . . f f e e e e f 2 2 2 f . . 
        . . . f e e e f f e e e e f . . 
        . . . f f f f e e 2 2 2 2 e f . 
        . . . f e 2 2 2 f f f f e 2 f . 
        . . f f f f f f f e e e f f f . 
        . . f f e 4 4 e b f 4 4 e e f . 
        . . f e e 4 d 4 1 f d d e f . . 
        . . . f e e e 4 d d d d f . . . 
        . . . . f f e e 4 4 4 e f . . . 
        . . . . . 4 d d e 2 2 2 f . . . 
        . . . . . e d d e 2 2 2 f . . . 
        . . . . . f e e f 4 5 5 f . . . 
        . . . . . . f f f f f f . . . . 
        . . . . . . . f f f . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f . . . . 
        . . . . f f e e e e f 2 f . . . 
        . . . f f e e e e f 2 2 2 f . . 
        . . . f e e e f f e e e e f . . 
        . . . f f f f e e 2 2 2 2 e f . 
        . . . f e 2 2 2 f f f f e 2 f . 
        . . f f f f f f f e e e f f f . 
        . . f f e 4 4 e b f 4 4 e e f . 
        . . f e e 4 d 4 1 f d d e f . . 
        . . . f e e e e e d d d f . . . 
        . . . . . f 4 d d e 4 e f . . . 
        . . . . . f e d d e 2 2 f . . . 
        . . . . f f f e e f 5 5 f f . . 
        . . . . f f f f f f f f f f . . 
        . . . . . f f . . . f f f . . . 
        `,img`
        . . . . . . f f f f f f . . . . 
        . . . . f f e e e e f 2 f . . . 
        . . . f f e e e e f 2 2 2 f . . 
        . . . f e e e f f e e e e f . . 
        . . . f f f f e e 2 2 2 2 e f . 
        . . . f e 2 2 2 f f f f e 2 f . 
        . . f f f f f f f e e e f f f . 
        . . f f e 4 4 e b f 4 4 e e f . 
        . . f e e 4 d 4 1 f d d e f . . 
        . . . f e e e 4 d d d d f . . . 
        . . . . f f e e 4 4 4 e f . . . 
        . . . . . 4 d d e 2 2 2 f . . . 
        . . . . . e d d e 2 2 2 f . . . 
        . . . . . f e e f 4 5 5 f . . . 
        . . . . . . f f f f f f . . . . 
        . . . . . . . f f f . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f . . . . 
        . . . . f f e e e e f 2 f . . . 
        . . . f f e e e e f 2 2 2 f . . 
        . . . f e e e f f e e e e f . . 
        . . . f f f f e e 2 2 2 2 e f . 
        . . . f e 2 2 2 f f f f e 2 f . 
        . . f f f f f f f e e e f f f . 
        . . f f e 4 4 e b f 4 4 e e f . 
        . . f e e 4 d 4 1 f d d e f . . 
        . . . f e e e 4 d d d d f . . . 
        . . . . 4 d d e 4 4 4 e f . . . 
        . . . . e d d e 2 2 2 2 f . . . 
        . . . . f e e f 4 4 5 5 f f . . 
        . . . . f f f f f f f f f f . . 
        . . . . . f f . . . f f f . . . 
        `],
    280,
    false
    )
})
info.onScore(8000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.GOOMBA, function (sprite, otherSprite) {
    if (sprite.vy > 0 && !(sprite.isHittingTile(CollisionDirection.Bottom)) || sprite.vy < GOOMBA.top) {
        sprites.destroy(GOOMBA, effects.spray, 500)
        GOOMBA.vy = -50
        info.changeScoreBy(15)
        music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
    } else {
        info.changeLifeBy(-1)
        sprite.sayText("OUCH!", 500, false)
        music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
    }
})
info.onScore(4000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.CHECKPOINT, function (sprite, otherSprite) {
    info.changeScoreBy(100)
    sprites.destroy(sprite, effects.starField, 100)
    info.changeLifeBy(1)
})
info.onScore(2000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
info.onLifeZero(function () {
    game.gameOver(false)
    game.setGameOverMessage(false, "GAME OVER!")
    game.setGameOverEffect(false, effects.dissolve)
})
info.onScore(7000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.LAVA, function (sprite3, otherSprite3) {
    info.changeLifeBy(-1000)
})
info.onScore(5000, function () {
    info.changeLifeBy(1)
    info.setScore(0)
})
let JUMP = false
let BAT_FLYING_ANIMATION: animation.Animation = null
let BAT_IDLE_ANIMATION: animation.Animation = null
let BAT: Sprite = null
let GOOMBA: Sprite = null
let LONGSAND: Sprite = null
let SLEEPING_DUCKY: Sprite = null
let THESAND: Sprite = null
let THESEAWEED1: Sprite = null
let THESEAWEED2: Sprite = null
let SEA: Sprite = null
let THESEASURFACE: Sprite = null
let THESEAWEED3: Sprite = null
let THETREASURECHEST: Sprite = null
let THELAVA: Sprite = null
let COIN_SPRITE: Sprite = null
let THEPLATFORMER: Sprite = null
scene.setBackgroundImage(assets.image`TEST WORLD - BACKGROUND`)
tiles.setCurrentTilemap(tilemap`Level - TEST WORLD`)
THEPLATFORMER = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . f f f f f f . . . . . 
    . . . f f e e e e f 2 f . . . . 
    . . f f e e e e f 2 2 2 f . . . 
    . . f e e e f f e e e e f . . . 
    . . f f f f e e 2 2 2 2 e f . . 
    . . f e 2 2 2 f f f f e 2 f . . 
    . f f f f f f f e e e f f f . . 
    . f f e 4 4 e b f 4 4 e e f . . 
    . f e e 4 d 4 1 f d d e f . . . 
    . . f e e e e e d d d f . . . . 
    . . . . f 4 d d e 4 e f . . . . 
    . . . . f e d d e 2 2 f . . . . 
    . . . f f f e e f 5 5 f f . . . 
    . . . f f f f f f f f f f . . . 
    . . . . f f . . . f f f . . . . 
    `, SpriteKind.Player)
scene.cameraFollowSprite(THEPLATFORMER)
controller.moveSprite(THEPLATFORMER, 80, 0)
THEPLATFORMER.ay = 300
info.setScore(0)
info.setLife(5)
for (let value of tiles.getTilesByType(sprites.dungeon.collectibleRedCrystal)) {
    COIN_SPRITE = sprites.create(img`
        . . b b b b . . 
        . b 5 5 5 5 b . 
        b 5 d 3 3 d 5 b 
        b 5 3 5 5 1 5 b 
        c 5 3 5 5 1 d c 
        c d d 1 1 d d c 
        . f d d d d f . 
        . . f f f f . . 
        `, SpriteKind.COIN)
    tiles.placeOnTile(COIN_SPRITE, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
    animation.runImageAnimation(
    COIN_SPRITE,
    [img`
        . . b b b b . . 
        . b 5 5 5 5 b . 
        b 5 d 3 3 d 5 b 
        b 5 3 5 5 1 5 b 
        c 5 3 5 5 1 d c 
        c d d 1 1 d d c 
        . f d d d d f . 
        . . f f f f . . 
        `,img`
        . . b b b . . . 
        . b 5 5 5 b . . 
        b 5 d 3 d 5 b . 
        b 5 3 5 1 5 b . 
        c 5 3 5 1 d c . 
        c 5 d 1 d d c . 
        . f d d d f . . 
        . . f f f . . . 
        `,img`
        . . . b b . . . 
        . . b 5 5 b . . 
        . b 5 d 1 5 b . 
        . b 5 3 1 5 b . 
        . c 5 3 1 d c . 
        . c 5 1 d d c . 
        . . f d d f . . 
        . . . f f . . . 
        `,img`
        . . . b b . . . 
        . . b 5 5 b . . 
        . . b 1 1 b . . 
        . . b 5 5 b . . 
        . . b d d b . . 
        . . c d d c . . 
        . . c 3 3 c . . 
        . . . f f . . . 
        `,img`
        . . . b b . . . 
        . . b 5 5 b . . 
        . b 5 1 d 5 b . 
        . b 5 1 3 5 b . 
        . c d 1 3 5 c . 
        . c d d 1 5 c . 
        . . f d d f . . 
        . . . f f . . . 
        `,img`
        . . . b b b . . 
        . . b 5 5 5 b . 
        . b 5 d 3 d 5 b 
        . b 5 1 5 3 5 b 
        . c d 1 5 3 5 c 
        . c d d 1 d 5 c 
        . . f d d d f . 
        . . . f f f . . 
        `],
    150,
    true
    )
}
for (let value2 of tiles.getTilesByType(sprites.dungeon.collectibleBlueCrystal)) {
    THELAVA = sprites.create(img`
        5 5 4 2 2 2 2 2 4 2 2 2 2 4 4 5 
        5 4 2 2 2 2 2 4 4 4 4 4 4 4 5 5 
        4 2 2 4 2 4 4 4 5 5 5 5 5 5 4 4 
        2 2 2 2 4 4 5 5 4 4 4 5 4 5 4 4 
        4 4 2 4 4 5 5 4 4 2 2 4 5 4 4 2 
        4 4 2 4 5 4 4 2 2 2 2 4 5 4 4 2 
        2 2 4 5 4 4 2 2 2 4 4 2 5 5 4 2 
        4 4 5 5 4 2 2 2 2 4 4 2 4 5 5 4 
        5 5 5 4 2 2 4 2 2 2 2 2 4 5 5 5 
        4 5 4 4 2 2 2 2 2 2 2 2 4 5 4 4 
        5 5 5 2 2 4 2 2 2 4 2 2 4 5 5 4 
        4 5 4 2 4 2 4 2 2 2 2 4 5 5 5 5 
        4 5 5 4 2 4 2 2 2 2 2 4 5 4 4 4 
        4 5 5 5 2 2 2 4 4 4 5 5 5 4 2 2 
        4 5 5 4 5 5 5 5 5 5 5 4 4 2 2 2 
        4 5 5 4 4 4 4 4 4 4 4 2 2 2 4 4 
        `, SpriteKind.LAVA)
    tiles.placeOnTile(THELAVA, value2)
    tiles.setTileAt(value2, assets.tile`transparency16`)
}
for (let value3 of tiles.getTilesByType(sprites.dungeon.chestClosed)) {
    THETREASURECHEST = sprites.create(img`
        . . b b b b b b b b b b b b . . 
        . b e 4 4 4 4 4 4 4 4 4 4 e b . 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e e 4 4 4 4 4 4 4 4 4 4 e e b 
        b e e e e e e e e e e e e e e b 
        b e e e e e e e e e e e e e e b 
        b b b b b b b d d b b b b b b b 
        c b b b b b b c c b b b b b b c 
        c c c c c c b c c b c c c c c c 
        b e e e e e c b b c e e e e e b 
        b e e e e e e e e e e e e e e b 
        b c e e e e e e e e e e e e c b 
        b b b b b b b b b b b b b b b b 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.TREASURECHEST)
    tiles.placeOnTile(THETREASURECHEST, value3)
    tiles.setTileAt(value3, assets.tile`transparency16`)
}
for (let value4 of tiles.getTilesByType(sprites.dungeon.doorOpenNorth)) {
    tiles.placeOnTile(THEPLATFORMER, value4)
}
for (let value5 of tiles.getTilesByType(sprites.dungeon.hazardHole)) {
    THESEAWEED3 = sprites.create(img`
        999999999999999999988999999999999999999999999999
        999999999999999999986899999999999999999999999999
        999999999999999999998689999999999999999999999999
        999999999999999999999868999999999999999999999999
        999999999999999999999986899999999999999999999999
        99999fff9999999999999986899999999999999999999999
        9999f.11f999999999999998689999999999999999999999
        9999f..1f999999999999998689999999999999999999999
        9999f...f999999999999998668999999999999999999999
        99999fff9999999999999998668999999999999999999999
        999999999999999999999998668999999999999999999999
        999999999999999999999998768999999999999999999999
        999999999999999999999998768999999999999999999999
        999999999999999999999986768999999999999999999999
        999999999999999999999987768999999999999999999999
        999999999999999999999967789999999999999999999999
        9999999999999999999996767699999999999fff99999999
        999999999999999999999676769999999999f.11f9999999
        999999999fff999999996565699999999999f..1f9999999
        99999999f.11f99999965565699999999999f...f9999999
        99999999f..1f999999656569999999999999fff99999999
        99999999f...f99999876756999999999999999999999999
        999999999fff999998767769998999999999999999999999
        999999999999999996767899998999999999999999999999
        999999999999999987666899988999999999999999999999
        999999999999999967868999986999999999999999999999
        999999999999999986868999876999999999999999999999
        999999999999999868668998768999999999999999999999
        999999999999999868689987678999fff999999999999999
        99999999999999986868998766999f.11f99999999999999
        99999999999999986868987678999f..1f99999999999999
        99999999999999986878987669999f...f99999999999999
        999999999999999878789767899999fff999999999999999
        999999999999999876768768988999999999999999999999
        999999999999999876778668967899999999999999999999
        999999999999999876676668996789999999999999999999
        999999999999999967677866899678999999999999999999
        999999999999999987667786689677899999999999999999
        999999999999999987766768888567899999999999999999
        999999999999999999766776888565699999999999999999
        999999999999999999676677888785699999999999999999
        999999999999999999877667787687699999999999999999
        999999999999999999987766776866899999999999999999
        999999999999999999998776676866899999999999999999
        999999999999999999999877677668999999999999999999
        999999999999999999999987667668999999999999999999
        999999999999999999999998767689999999999999999999
        999999999999999999999998768899999999999999999999
        `, SpriteKind.SEAWEEDTHREE)
    tiles.placeOnTile(THESEAWEED3, value5)
    tiles.setTileAt(value5, assets.tile`transparency16`)
}
for (let value6 of tiles.getTilesByType(sprites.swamp.swampTile10)) {
    THESEASURFACE = sprites.create(img`
        c c c c c c c c c c c c c c c c 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 6 6 6 8 8 8 6 6 6 6 8 8 8 
        6 6 8 8 8 6 6 6 6 6 6 8 8 8 8 6 
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
        9 9 6 6 6 6 6 9 9 9 9 6 6 6 9 9 
        6 6 6 6 9 9 9 6 6 6 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        `, SpriteKind.SEA1)
    tiles.placeOnTile(THESEASURFACE, value6)
    tiles.setTileAt(value6, assets.tile`transparency16`)
}
for (let value7 of tiles.getTilesByType(sprites.swamp.swampTile16)) {
    SEA = sprites.create(img`
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        `, SpriteKind.SEA2)
    tiles.placeOnTile(SEA, value7)
    tiles.setTileAt(value7, assets.tile`transparency16`)
}
for (let value8 of tiles.getTilesByType(sprites.swamp.swampTile8)) {
    THESEAWEED2 = sprites.create(img`
        9999999998889999
        9999999886689999
        9999998668899999
        9999987689999999
        9999877899999999
        999987789fff9999
        99987789f.11f999
        99985789f..1f999
        99985589f...f999
        999875899fff9889
        9998767899998789
        9998767899987899
        9999876789876899
        9fff876768678999
        f.11f87668778999
        f..1f98668766999
        f...f99868767899
        9fff999986676789
        9999999986857569
        9999889986665756
        9998689986685656
        9986689986687678
        9866899868687678
        9868998688667678
        8768988886876778
        8768988888776789
        8766888886767789
        8767688866877899
        9876776868668999
        9877667788689999
        9987766768899999
        9998676778899999
        `, SpriteKind.SEAWEEDTWO)
    tiles.placeOnTile(THESEAWEED2, value8)
    tiles.setTileAt(value8, assets.tile`transparency16`)
}
for (let value10 of tiles.getTilesByType(sprites.swamp.swampTile4)) {
    THESEAWEED1 = sprites.create(img`
        9 9 9 9 9 8 8 9 9 9 9 9 f f f 9 
        9 9 9 9 9 8 6 8 9 9 9 f . 1 1 f 
        9 f f f 9 9 8 6 8 9 9 f . . 1 f 
        f . 1 1 f 9 9 8 6 8 9 f . . . f 
        f . . 1 f 9 9 8 6 6 9 9 f f f 9 
        f . . . f 9 9 8 6 7 6 9 9 9 9 9 
        9 f f f 9 9 6 7 6 5 6 9 9 9 9 9 
        9 9 9 9 9 6 5 6 7 5 8 9 9 9 9 9 
        9 9 9 9 6 5 7 7 5 8 6 8 9 9 9 9 
        9 9 9 9 6 5 6 5 6 8 6 8 9 9 9 9 
        9 9 9 9 8 7 6 7 8 8 6 8 9 9 9 9 
        9 9 9 9 8 7 6 7 8 6 6 8 9 9 9 9 
        9 9 9 9 8 7 6 7 7 6 6 8 9 9 9 9 
        9 9 9 9 8 7 7 6 7 6 8 9 9 9 9 9 
        9 9 9 9 9 8 7 6 7 8 9 9 9 9 9 9 
        9 9 9 9 9 9 8 7 6 8 9 9 9 9 9 9 
        `, SpriteKind.SEAWEED1)
    tiles.placeOnTile(THESEAWEED1, value10)
    tiles.setTileAt(value10, assets.tile`transparency16`)
}
for (let value9 of tiles.getTilesByType(sprites.swamp.swampTile6)) {
    THESAND = sprites.create(img`
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d 
        d d d d d b d d d d d d d d d d 
        b b b b b b b b b b d d b b b b 
        c c b b b c c b b b b b b b c c 
        c c c c c c c c c c c c c c c c 
        `, SpriteKind.SAND)
    tiles.placeOnTile(THESAND, value9)
    tiles.setTileAt(value9, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(sprites.skillmap.islandTile5)) {
    SLEEPING_DUCKY = sprites.create(img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 d 4 c . . 
        . . . . b 5 5 1 f f d d 4 4 4 b 
        . . . . b 5 5 d f b 4 4 4 4 b . 
        . . . b d 5 5 5 5 4 4 4 4 b . . 
        . . b d d 5 5 5 5 5 5 5 5 b . . 
        . b d d d d 5 5 5 5 5 5 5 5 b . 
        b d d d b b b 5 5 5 5 5 5 5 b . 
        c d d b 5 5 d c 5 5 5 5 5 5 b . 
        c b b d 5 d c d 5 5 5 5 5 5 b . 
        . b 5 5 b c d d 5 5 5 5 5 d b . 
        . . c c c d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        `, SpriteKind.DUCKY)
    tiles.placeOnTile(SLEEPING_DUCKY, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
    animation.runImageAnimation(
    SLEEPING_DUCKY,
    [img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . b 5 5 b . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . b b b b b 5 5 5 5 5 5 5 b . . 
        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
        . . b d 5 5 b 1 f f 5 4 4 c . . 
        b b d b 5 5 5 d f b 4 4 4 4 b . 
        b d d c d 5 5 b 5 4 4 4 4 4 4 b 
        c d d d c c b 5 5 5 5 5 5 5 b . 
        c b d d d d d 5 5 5 5 5 5 5 b . 
        . c d d d d d d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        `,img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . b b b b b 5 5 5 5 5 5 5 b . . 
        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
        . . b d 5 5 b 1 f f 5 4 4 c . . 
        b b d b 5 5 5 d f b 4 4 4 4 4 b 
        b d d c d 5 5 b 5 4 4 4 4 4 b . 
        c d d d c c b 5 5 5 5 5 5 5 b . 
        c b d d d d d 5 5 5 5 5 5 5 b . 
        . c d d d d d d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        `,img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . . . . b c . . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 5 d f . . 
        . . . . b 5 5 1 f f 5 d 4 c . . 
        . . . . b 5 5 d f b d d 4 4 . . 
        b d d d b b d 5 5 5 4 4 4 4 4 b 
        b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
        b d c 5 5 5 5 d 5 5 5 5 5 b . . 
        c d d c d 5 5 b 5 5 5 5 5 5 b . 
        c b d d c c b 5 5 5 5 5 5 5 b . 
        . c d d d d d d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        `,img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 d 4 c . . 
        . . . . b 5 5 1 f f d d 4 4 4 b 
        . . . . b 5 5 d f b 4 4 4 4 b . 
        . . . b d 5 5 5 5 4 4 4 4 b . . 
        . . b d d 5 5 5 5 5 5 5 5 b . . 
        . b d d d d 5 5 5 5 5 5 5 5 b . 
        b d d d b b b 5 5 5 5 5 5 5 b . 
        c d d b 5 5 d c 5 5 5 5 5 5 b . 
        c b b d 5 d c d 5 5 5 5 5 5 b . 
        . b 5 5 b c d d 5 5 5 5 5 d b . 
        b b c c c d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        `,img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 d 4 c . . 
        . . . . b 5 5 1 f f d d 4 4 4 b 
        . . . . b 5 5 d f b 4 4 4 4 b . 
        . . . b d 5 5 5 5 4 4 4 4 b . . 
        . b b d d d 5 5 5 5 5 5 5 b . . 
        b d d d b b b 5 5 5 5 5 5 5 b . 
        c d d b 5 5 d c 5 5 5 5 5 5 b . 
        c b b d 5 d c d 5 5 5 5 5 5 b . 
        c b 5 5 b c d d 5 5 5 5 5 5 b . 
        b b c c c d d d 5 5 5 5 5 d b . 
        . . . . c c d d d 5 5 5 b b . . 
        . . . . . . c c c c c b b . . . 
        `,img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 5 d f . . 
        . . . . b 5 5 1 f f 5 d 4 c . . 
        . . . . b 5 5 d f b d d 4 4 . . 
        . b b b d 5 5 5 5 5 4 4 4 4 4 b 
        b d d d b b d 5 5 4 4 4 4 4 b . 
        b b d 5 5 5 b 5 5 5 5 5 5 b . . 
        c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
        c b d c d 5 5 b 5 5 5 5 5 5 b . 
        . c d d c c b d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        . . . . . . . . . . . . . . . . 
        `],
    100,
    true
    )
}
for (let value12 of tiles.getTilesByType(sprites.swamp.swampTile5)) {
    LONGSAND = sprites.create(img`
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddddddddddddd
        dddddbbddddddddd
        bbbbbbbbbbddbbbb
        ccbbbccbbbbbbbcc
        cccccccccccccccc
        `, SpriteKind.SAND2)
    tiles.placeOnTile(LONGSAND, value12)
    tiles.setTileAt(value12, assets.tile`transparency16`)
}
for (let value of tiles.getTilesByType(sprites.swamp.swampTile11)) {
    SLEEPING_DUCKY = sprites.create(img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . . . . b c . . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 5 5 5 5 5 d b . . 
        . . . . b 5 5 f f 5 5 d 4 f . . 
        . . . . b 5 5 5 5 5 d d 4 4 . . 
        b d d d b b d 5 5 5 4 4 4 4 4 b 
        b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
        b d c 5 5 5 5 d 5 5 5 5 5 b . . 
        c d d c d 5 5 b 5 5 5 5 5 5 b . 
        c b d d c c b 5 5 5 5 5 5 5 b . 
        . c d d d d d d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . . 
        `, SpriteKind.SLEEPYRUBBERDUCKY)
    tiles.placeOnTile(SLEEPING_DUCKY, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
}
for (let value of tiles.getTilesByType(assets.tile`myTile7`)) {
    GOOMBA = sprites.create(assets.tile`myTile7`, SpriteKind.GOOMBA)
    tiles.placeOnTile(GOOMBA, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
    GOOMBA.ay = 200
    if (Math.percentChance(50)) {
        GOOMBA.ax = randint(30, 60)
    } else {
        GOOMBA.ax = randint(-60, -30)
    }
}
for (let value of tiles.getTilesByType(assets.tile`myTile8`)) {
    BAT = sprites.create(assets.tile`myTile8`, SpriteKind.BAT)
    tiles.placeOnTile(BAT, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
    BAT.ay = 200
    BAT_IDLE_ANIMATION = animation.createAnimation(ActionKind.Walking, 100)
    BAT_IDLE_ANIMATION.addAnimationFrame(img`
        . . f f f . . . . . . . . f f f 
        . f f c c . . . . . . f c b b c 
        f f c c . . . . . . f c b b c . 
        f c f c . . . . . . f b c c c . 
        f f f c c . c c . f c b b c c . 
        f f c 3 c c 3 c c f b c b b c . 
        f f b 3 b c 3 b c f b c c b c . 
        . c b b b b b b c b b c c c . . 
        . c 1 b b b 1 b b c c c c . . . 
        c b b b b b b b b b c c . . . . 
        c b c b b b c b b b b f . . . . 
        f b 1 f f f 1 b b b b f c . . . 
        f b b b b b b b b b b f c c . . 
        . f b b b b b b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        `)
    BAT_FLYING_ANIMATION = animation.createAnimation(ActionKind.Walking, 100)
    BAT_FLYING_ANIMATION.addAnimationFrame(img`
        . . f f f . . . . . . . . f f f 
        . f f c c . . . . . . f c b b c 
        f f c c . . . . . . f c b b c . 
        f c f c . . . . . . f b c c c . 
        f f f c c . c c . f c b b c c . 
        f f c 3 c c 3 c c f b c b b c . 
        f f b 3 b c 3 b c f b c c b c . 
        . c b b b b b b c b b c c c . . 
        . c 1 b b b 1 b b c c c c . . . 
        c b b b b b b b b b c c . . . . 
        c b c b b b c b b b b f . . . . 
        f b 1 f f f 1 b b b b f c . . . 
        f b b b b b b b b b b f c c . . 
        . f b b b b b b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        `)
    BAT_FLYING_ANIMATION.addAnimationFrame(img`
        . . f f f . . . . . . . . . . . 
        f f f c c . . . . . . . . f f f 
        f f c c . . c c . . . f c b b c 
        f f c 3 c c 3 c c f f b b b c . 
        f f b 3 b c 3 b c f b b c c c . 
        . c b b b b b b c f b c b c c . 
        . c b b b b b b c b b c b b c . 
        c b 1 b b b 1 b b b c c c b c . 
        c b b b b b b b b c c c c c . . 
        f b c b b b c b b b b f c . . . 
        f b 1 f f f 1 b b b b f c c . . 
        . f b b b b b b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `)
    BAT_FLYING_ANIMATION.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . c c . . c c . . . . . . . . 
        . . c 3 c c 3 c c c . . . . . . 
        . c b 3 b c 3 b c c c . . . . . 
        . c b b b b b b b b f f . . . . 
        c c b b b b b b b b f f . . . . 
        c b 1 b b b 1 b b c f f f . . . 
        c b b b b b b b b f f f f . . . 
        f b c b b b c b c c b b b . . . 
        f b 1 f f f 1 b f c c c c . . . 
        . f b b b b b b f b b c c . . . 
        c c f b b b b b c c b b c . . . 
        c c c f f f f f f c c b b c . . 
        . c c c . . . . . . c c c c c . 
        . . c c c . . . . . . . c c c c 
        . . . . . . . . . . . . . . . . 
        `)
    BAT_FLYING_ANIMATION.addAnimationFrame(img`
        . f f f . . . . . . . . f f f . 
        f f c . . . . . . . f c b b c . 
        f c c . . . . . . f c b b c . . 
        c f . . . . . . . f b c c c . . 
        c f f . . . . . f f b b c c . . 
        f f f c c . c c f b c b b c . . 
        f f f c c c c c f b c c b c . . 
        . f c 3 c c 3 b c b c c c . . . 
        . c b 3 b c 3 b b c c c c . . . 
        c c b b b b b b b b c c . . . . 
        c b 1 b b b 1 b b b b f c . . . 
        f b b b b b b b b b b f c c . . 
        f b c b b b c b b b b f . . . . 
        . f 1 f f f 1 b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        `)
    animation.attachAnimation(BAT, BAT_FLYING_ANIMATION)
    animation.attachAnimation(BAT, BAT_IDLE_ANIMATION)
}
if (THEPLATFORMER.vx < 0 || THEPLATFORMER.x > scene.screenWidth()) {
    THEPLATFORMER.vx = THEPLATFORMER.vx * -1
}
game.setDialogFrame(img`
    ..................................................................
    ....33.......33...........dddd............dddd............aaa.....
    ...a533.....393....ddddddd1111d....ddddddd1111d....3333...a35a....
    ...a553aaa339993.dd1111dd111111dddd1111dd111111dd.39393aaa3553aa..
    ..a355555a3999993d11911111111111dd11911111111111d339993a555555553.
    .a555555333399933119991111111111111999111111111113999993a55555533.
    .a355555333393931111911111115511111191111111551111399933a3555533..
    .aa355555a1333311111111111115511111111111111551111339331a55555a...
    ...a55355a1111111111111111111111111111111111111111133311a55335a...
    ...a5aaaaa1111191111111111111111111111111111111111111111aaa33aa...
    ...aa3311115511111111111111111111111111111111111119111111113333...
    ..3339331115511111111111111111111111111111111111111111551133393...
    ..39999331111111111111111111111111111111111111111111115511399993..
    ..339999311111111111111111111111111111111111111111111111113399993.
    ..399993311111111111111111111111111111111111111111111111113999933.
    ...339331191111111111111111111111111111111111111111111119113393...
    ....3311111111111111111111111111111111111111111111111111111133....
    ...dd11111111111111111111111111111111111111111111111111111111dd...
    ...d1111111111111111111111111111111111111111111111111111111111d...
    ..d111111111111111111111111111111111111111111111111111111111911d..
    .d1111551111111111111111111111111111111111111111111111111119991d..
    .d1111551111111111111111111111111111111111111111111111111111911d..
    .d1111111111111111111111111111111111111111111111111111111111111d..
    .d111111111111111111111111111111111111111111111111111111111111dd..
    ..d11111111111111111111111111111111111111111111111111111111111dd..
    ..dd11111111111111111111111111111111111111111111111111111111111d..
    ..dd111111111111111111111111111111111111111111111111111111111111d.
    ..d1111111111111111111111111111111111111111111111111111111111111d.
    ..d1191111111111111111111111111111111111111111111111111111551111d.
    ..d1999111111111111111111111111111111111111111111111111111551111d.
    ..d119111111111111111111111111111111111111111111111111111111111d..
    ...d1111111111111111111111111111111111111111111111111111111111d...
    ...dd11111111111111111111111111111111111111111111111111111111dd...
    ...dd11111111111111111111111111111111111111111111111111111111dd...
    ...d1111111111111111111111111111111111111111111111111111111111d...
    ..d111111111111111111111111111111111111111111111111111111111911d..
    .d1111551111111111111111111111111111111111111111111111111119991d..
    .d1111551111111111111111111111111111111111111111111111111111911d..
    .d1111111111111111111111111111111111111111111111111111111111111d..
    .d111111111111111111111111111111111111111111111111111111111111dd..
    ..d11111111111111111111111111111111111111111111111111111111111dd..
    ..dd11111111111111111111111111111111111111111111111111111111111d..
    ..dd111111111111111111111111111111111111111111111111111111111111d.
    ..d1111111111111111111111111111111111111111111111111111111111111d.
    ..d1191111111111111111111111111111111111111111111111111111551111d.
    ..d1999111111111111111111111111111111111111111111111111111551111d.
    ..d119111111111111111111111111111111111111111111111111111111111d..
    ...d1111111111111111111111111111111111111111111111111111111111d...
    ...dd11111111111111111111111111111111111111111111111111111111dd...
    ....3311111111111111111111111111111111111111111111111111111133....
    ...393311911111111111111111111111111111111111111111111191133933...
    .339999311111111111111111111111111111111111111111111111113399993..
    .399993311111111111111111111111111111111111111111111111113999933..
    ..39999311551111111111111111111111111111111111111111111113399993..
    ...3933311551111111111111111111111111111111111111111155111339333..
    ...3333111111119111111111111111111111111111111111111155111133aa...
    ...aa33aaa1111111111111111111111111111111111111111911111aaaaa5a...
    ...a53355a1133311111111111111111111111111111111111111111a55355a...
    ...a55555a1339331111551111111111111155111111111111133331a555553aa.
    ..3355553a339993111155111111191111115511111119111139393333555553a.
    .33555555a399999311111111111999111111111111199911339993333555555a.
    .355555555a399933d11111111111911dd11111111111911d3999993a555553a..
    ..aa3553aaa39393.dd111111dd1111dddd111111dd1111dd.399933aaa355a...
    ....a53a...3333....d1111ddddddd....d1111ddddddd....393.....335a...
    .....aaa............dddd............dddd...........33.......33....
    ..................................................................
    `)
game.setDialogCursor(img`
    . . . . . . . . f . . . . . . . 
    . . . . . . . f b f . . . . . . 
    . . . . . . f b d b f . . . . . 
    . . . . . . f 4 d 4 f . . . . . 
    . . . . . . f 4 5 4 f . . . . . 
    . . . f f f 2 d 5 d 2 f f f . . 
    . . f b 4 4 d 5 5 5 d 4 4 b f . 
    . f b d d 5 5 5 5 5 5 5 d d b f 
    . . f b 4 4 d 5 5 5 d 4 4 b f . 
    . . . f f f 2 d 5 d 2 f f f . . 
    . . . . . . f 4 5 4 f . . . . . 
    . . . . . . f 4 d 4 f . . . . . 
    . . . . . . f b d b f . . . . . 
    . . . . . . . f b f . . . . . . 
    . . . . . . . . f . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `)
game.showLongText("Wassup! I'm Jay, the creator of this platforming game!", DialogLayout.Bottom)
game.showLongText("You can move using the right and left buttons.", DialogLayout.Bottom)
game.showLongText("Additionally, you can also jump by pressing the space / 'A' button.", DialogLayout.Bottom)
game.showLongText("If you would want to double jump, press the space /'A' button again in Mid-air", DialogLayout.Bottom)
game.showLongText("On some occasions, there will be a Treasure Chest hidden across the map.", DialogLayout.Bottom)
game.showLongText("Hope that you'll have fun!", DialogLayout.Bottom)
