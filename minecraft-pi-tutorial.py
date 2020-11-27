from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.postToChat("Script is starting...")

PlayerX, PlayerY, PlayerZ = mc.player.getPos()
#mc.player.setPos(x, y, z)

mc.setBlock(PlayerX, PlayerY + 2, PlayerZ, block.STONE.id)
#mc.setBlocks(x0, y0, z0, x1, y1, z1, id)
#mc.getBlock(x, y, z)

#block.WOOL.id 1 -> color
#block.TNT.id 1 -> activated