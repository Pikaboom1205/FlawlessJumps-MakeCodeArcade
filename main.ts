enum ActionKind {
    Walking,
    Idle,
    Jumping,
    FLYING_BAT
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
    export const ARROW = SpriteKind.create()
    export const POISON = SpriteKind.create()
    export const LEVELCOMPLETIONPOINT_ = SpriteKind.create()
    export const QUESTIONMARKBLOCK = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.SEAWEEDTHREE, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1000)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.LEVELCOMPLETIONPOINT_, function (sprite, otherSprite) {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
    game.setGameOverMessage(true, "GOOD JOB PLAYER_01! YOU DID IT!")
    game.setGameOverScoringType(game.ScoringType.HighScore)
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
    sprites.destroy(otherSprite7, effects.fountain, 50)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.STAR, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.UntilDone)
    info.changeScoreBy(150)
    sprites.destroy(otherSprite, effects.fire, 500)
    info.changeLifeBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SAND, function (sprite4, otherSprite4) {
    info.changeLifeBy(-1000)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.setVolume(255)
    if (THEPLATFORMER.isHittingTile(CollisionDirection.Bottom)) {
        music.play(music.createSoundEffect(
        WaveShape.Square,
        400,
        600,
        255,
        0,
        100,
        SoundExpressionEffect.None,
        InterpolationCurve.Linear
        ), music.PlaybackMode.InBackground)
        THEPLATFORMER.vy = -110
        JUMP = true
    } else if (JUMP == true) {
        THEPLATFORMER.startEffect(effects.trail, 1000)
        music.play(music.createSoundEffect(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        scene.cameraShake(2, 500)
        THEPLATFORMER.vy = -110
        JUMP = false
    }
    if (THEPLATFORMER.vy == 0) {
        THEPLATFORMER.vy = 110
        if (controller.left.isPressed()) {
            animation.runImageAnimation(
            THEPLATFORMER,
            assets.animation`MAINCHARACTER_LEFTMOVE`,
            280,
            true
            )
        }
        if (controller.right.isPressed()) {
            animation.runImageAnimation(
            THEPLATFORMER,
            assets.animation`MAINCHRACTER_RIGHTMOVE`,
            280,
            true
            )
        }
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    THEPLATFORMER,
    assets.animation`MORE_FRAMES_MOVELEFT`,
    280,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SAND2, function (sprite6, otherSprite6) {
    info.changeLifeBy(-1000)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SEA1, function (sprite5, otherSprite5) {
    info.changeLifeBy(-1000)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    THEPLATFORMER,
    assets.animation`MORE_FRAMES_MOVERIGHT`,
    280,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.GOOMBA, function (sprite, otherSprite) {
    if (sprite.vy > 0 && !(sprite.isHittingTile(CollisionDirection.Bottom)) || sprite.y < otherSprite.top) {
        sprites.destroy(otherSprite, effects.spray, 500)
        sprite.vy = -50
        info.changeScoreBy(15)
        music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
    } else {
        info.changeLifeBy(-1)
        sprite.sayText("OUCH!", 500, false)
        music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.CHECKPOINT, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
    info.changeScoreBy(100)
    sprites.destroy(otherSprite, effects.fire, 500)
    info.changeLifeBy(1)
})
info.onLifeZero(function () {
    game.gameOver(false)
    game.setGameOverMessage(false, "GAME OVER!")
    game.setGameOverEffect(false, effects.dissolve)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.LAVA, function (sprite3, otherSprite3) {
    info.changeLifeBy(-1000)
})
scene.onHitWall(SpriteKind.GOOMBA, function (sprite, location) {
    GOOMBA.image.flipX()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.BAT, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprite.sayText("OUCH!", 500, false)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
    animation.runImageAnimation(
    otherSprite,
    assets.animation`BAT_LEFT_ANIMATION`,
    200,
    false
    )
    animation.runImageAnimation(
    otherSprite,
    assets.animation`BAT_RIGHT_ANIMATION`,
    200,
    false
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.POISON, function (sprite8, otherSprite8) {
    info.changeLifeBy(-1000)
})
let JUMP = false
let LEVELCOMPLETIONPOINT: Sprite = null
let POISON2: Sprite = null
let POISON1: Sprite = null
let STAR_SPRITESTAR: Sprite = null
let ARROW: Sprite = null
let CHECKPOINT: Sprite = null
let BAT: Sprite = null
let GOOMBA: Sprite = null
let SLEEPING_DUCKY: Sprite = null
let LONGSAND: Sprite = null
let RUBBERDUCKY: Sprite = null
let THESAND: Sprite = null
let THESEAWEED1: Sprite = null
let THESEAWEED2: Sprite = null
let SEA: Sprite = null
let THESEASURFACE: Sprite = null
let THESEAWEED3: Sprite = null
let THELAVA: Sprite = null
let COIN_SPRITE: Sprite = null
let THEPLATFORMER: Sprite = null
tiles.setCurrentTilemap(tilemap`Flawless Jumps - IntermediateFinalised`)
scene.setBackgroundImage(assets.image`Flawless Jumps - Background`)
let LEVEL_NO = 0
THEPLATFORMER = sprites.create(assets.image`JUMPY PLATFORMER`, SpriteKind.Player)
controller.moveSprite(THEPLATFORMER, 80, 0)
scene.cameraFollowSprite(THEPLATFORMER)
THEPLATFORMER.ay = 300
info.setScore(0)
info.setLife(5)
for (let value2 of tiles.getTilesByType(sprites.dungeon.collectibleRedCrystal)) {
    COIN_SPRITE = sprites.create(assets.image`COIN`, SpriteKind.COIN)
    tiles.placeOnTile(COIN_SPRITE, value2)
    tiles.setTileAt(value2, assets.tile`transparency16`)
    animation.runImageAnimation(
    COIN_SPRITE,
    assets.animation`COIN_ANIMATION`,
    150,
    true
    )
}
for (let value2 of tiles.getTilesByType(sprites.dungeon.collectibleBlueCrystal)) {
    THELAVA = sprites.create(assets.image`LAVA1`, SpriteKind.LAVA)
    tiles.placeOnTile(THELAVA, value2)
    tiles.setTileAt(value2, assets.tile`transparency16`)
}
for (let value4 of tiles.getTilesByType(sprites.dungeon.doorOpenNorth)) {
    tiles.placeOnTile(THEPLATFORMER, value4)
}
for (let value5 of tiles.getTilesByType(sprites.dungeon.hazardHole)) {
    THESEAWEED3 = sprites.create(assets.image`SEAWEED3_DRAWN`, SpriteKind.SEAWEEDTHREE)
    tiles.placeOnTile(THESEAWEED3, value5)
    tiles.setTileAt(value5, assets.tile`transparency16`)
}
for (let value6 of tiles.getTilesByType(sprites.swamp.swampTile10)) {
    THESEASURFACE = sprites.create(assets.image`OCEAN_SURFACE`, SpriteKind.SEA1)
    tiles.placeOnTile(THESEASURFACE, value6)
    tiles.setTileAt(value6, assets.tile`transparency16`)
}
for (let value7 of tiles.getTilesByType(sprites.swamp.swampTile16)) {
    SEA = sprites.create(assets.image`OCEAN`, SpriteKind.SEA2)
    tiles.placeOnTile(SEA, value7)
    tiles.setTileAt(value7, assets.tile`transparency16`)
}
for (let value8 of tiles.getTilesByType(sprites.swamp.swampTile8)) {
    THESEAWEED2 = sprites.create(assets.image`SEAWEED2_DRAWN`, SpriteKind.SEAWEEDTWO)
    tiles.placeOnTile(THESEAWEED2, value8)
    tiles.setTileAt(value8, assets.tile`transparency16`)
}
for (let value10 of tiles.getTilesByType(sprites.swamp.swampTile4)) {
    THESEAWEED1 = sprites.create(assets.image`SEAWEED1_DRAWN`, SpriteKind.SEAWEED1)
    tiles.placeOnTile(THESEAWEED1, value10)
    tiles.setTileAt(value10, assets.tile`transparency16`)
}
for (let value9 of tiles.getTilesByType(sprites.swamp.swampTile6)) {
    THESAND = sprites.create(assets.image`SAND_BASE`, SpriteKind.SAND)
    tiles.placeOnTile(THESAND, value9)
    tiles.setTileAt(value9, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(sprites.skillmap.islandTile5)) {
    RUBBERDUCKY = sprites.create(assets.image`UNUSED_DUCK`, SpriteKind.DUCKY)
    tiles.placeOnTile(RUBBERDUCKY, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
    animation.runImageAnimation(
    RUBBERDUCKY,
    assets.animation`SWIMMING_DUCK`,
    100,
    true
    )
}
for (let value12 of tiles.getTilesByType(sprites.swamp.swampTile5)) {
    LONGSAND = sprites.create(assets.image`SAND_EDITED`, SpriteKind.SAND2)
    tiles.placeOnTile(LONGSAND, value12)
    tiles.setTileAt(value12, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(sprites.swamp.swampTile11)) {
    SLEEPING_DUCKY = sprites.create(assets.image`SLEEPING_DUCK`, SpriteKind.SLEEPYRUBBERDUCKY)
    tiles.placeOnTile(SLEEPING_DUCKY, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(assets.tile`myTile7`)) {
    GOOMBA = sprites.create(assets.tile`myTile7`, SpriteKind.GOOMBA)
    tiles.placeOnTile(GOOMBA, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
    GOOMBA.ay = 200
    if (Math.percentChance(50)) {
        GOOMBA.ax = randint(30, 60)
    } else {
        GOOMBA.ax = randint(-60, -30)
    }
}
for (let value11 of tiles.getTilesByType(assets.tile`myTile8`)) {
    BAT = sprites.create(assets.tile`myTile8`, SpriteKind.BAT)
    tiles.placeOnTile(BAT, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
    BAT.ay = 200
}
for (let value11 of tiles.getTilesByType(assets.tile`CHECKPOINT`)) {
    CHECKPOINT = sprites.create(assets.image`CHECKPOINT_RED`, SpriteKind.CHECKPOINT)
    tiles.placeOnTile(CHECKPOINT, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(assets.tile`myTile9`)) {
    ARROW = sprites.create(assets.image`RAINBOW_POINTER`, SpriteKind.ARROW)
    tiles.placeOnTile(ARROW, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
    animation.runImageAnimation(
    ARROW,
    assets.animation`ARROW_RAINBOW`,
    100,
    true
    )
}
for (let value11 of tiles.getTilesByType(sprites.dungeon.collectibleInsignia)) {
    STAR_SPRITESTAR = sprites.create(assets.image`STAR`, SpriteKind.STAR)
    tiles.placeOnTile(STAR_SPRITESTAR, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(sprites.swamp.swampTile9)) {
    POISON1 = sprites.create(assets.image`POISON`, SpriteKind.POISON)
    tiles.placeOnTile(POISON1, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(sprites.swamp.swampTile13)) {
    POISON2 = sprites.create(assets.image`POISON_BUBBLES`, SpriteKind.POISON)
    tiles.placeOnTile(POISON2, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
}
for (let value11 of tiles.getTilesByType(assets.tile`CHECKPOINT2`)) {
    LEVELCOMPLETIONPOINT = sprites.create(assets.image`CHECKPOINT_BLUE_WORLDCOMPLETE`, SpriteKind.LEVELCOMPLETIONPOINT_)
    tiles.placeOnTile(LEVELCOMPLETIONPOINT, value11)
    tiles.setTileAt(value11, assets.tile`transparency16`)
}
if (THEPLATFORMER.vx < 0 || THEPLATFORMER.x > scene.screenWidth()) {
    THEPLATFORMER.vx = THEPLATFORMER.vx * -1
}
game.setDialogFrame(assets.image`TEXT_AREA`)
game.setDialogCursor(assets.image`COMETSTAR_POINTER`)
game.showLongText("You can move using the right and left buttons.", DialogLayout.Bottom)
game.showLongText("Additionally, you can also jump by pressing the space / 'A' button.", DialogLayout.Bottom)
game.showLongText("If you would want to double jump, press the space /'A' button again in Mid-air", DialogLayout.Bottom)
game.showLongText("On some occasions, there will be a [STAR] entity hidden across the map.", DialogLayout.Bottom)
game.showLongText("Hope that you'll have fun!", DialogLayout.Bottom)
game.onUpdate(function () {
    for (let BAT of sprites.allOfKind(SpriteKind.BAT)) {
        if (Math.abs(BAT.x - THEPLATFORMER.x) < 60) {
            let BAT_FLYING_ANIMATION = 0
            if (BAT.x - THEPLATFORMER.x < -5) {
                BAT.vx = 25
            } else if (BAT.x - THEPLATFORMER.x > 5) {
                BAT.vx = -25
            }
            if (BAT.y - THEPLATFORMER.y < -5) {
                BAT.vy = 25
            } else if (BAT.y - THEPLATFORMER.y > 5) {
                BAT.vy = -25
            }
            animation.setAction(BAT, BAT_FLYING_ANIMATION)
        } else {
            let BAT_IDLE_ANIMATION = 0
            BAT.vy = -20
            BAT.vx = 0
            animation.setAction(BAT, BAT_IDLE_ANIMATION)
        }
    }
    for (let GOOMBA of sprites.allOfKind(SpriteKind.GOOMBA)) {
        if (GOOMBA.isHittingTile(CollisionDirection.Left)) {
            GOOMBA.vx = 30
            GOOMBA.image.flipX()
        } else if (GOOMBA.isHittingTile(CollisionDirection.Right)) {
            GOOMBA.vx = -30
            GOOMBA.image.flipX()
        }
    }
})
game.onUpdateInterval(500, function () {
    if (GOOMBA.isHittingTile(CollisionDirection.Left)) {
        GOOMBA.ax = randint(30, 60)
    }
})
game.onUpdateInterval(500, function () {
    if (GOOMBA.isHittingTile(CollisionDirection.Right)) {
        GOOMBA.ax = randint(-60, -30)
    }
})
