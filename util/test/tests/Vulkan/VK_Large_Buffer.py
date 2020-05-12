import renderdoc as rd
import rdtest


class VK_Large_Buffer(rdtest.TestCase):
    demos_test_name = 'VK_Large_Buffer'

    def check_capture(self):
        draw = self.find_draw("Draw")

        self.controller.SetFrameEvent(draw.eventId, False)

        vsin_ref = {
            0: {
                'vtx': 0,
                'idx': 0,
                'Position': [-0.5, -0.5, 0.0],
                'Color': [0.0, 1.0, 0.0, 1.0],
                'UV': [0.0, 0.0],
            },
            1: {
                'vtx': 1,
                'idx': 1000000,
                'Position': [0.0, 0.5, 0.0],
                'Color': [0.0, 1.0, 0.0, 1.0],
                'UV': [0.0, 1.0],
            },
            2: {
                'vtx': 2,
                'idx': 2345678,
                'Position': [0.5, -0.5, 0.0],
                'Color': [0.0, 1.0, 0.0, 1.0],
                'UV': [1.0, 0.0],
            },
        }

        self.check_mesh_data(vsin_ref, self.get_vsin(draw))

        postvs_data = self.get_postvs(draw, rd.MeshDataStage.VSOut, 0, draw.numIndices)

        postvs_ref = {
            0: {
                'vtx': 0,
                'idx': 0,
                'gl_PerVertex_var.gl_Position': [-0.5, 0.5, 0.0, 1.0],
                'vertOut.pos': [-0.5, 0.5, 0.0, 1.0],
                'vertOut.col': [0.0, 1.0, 0.0, 1.0],
                'vertOut.uv': [0.0, 0.0, 0.0, 1.0],
            },
            1: {
                'vtx': 1,
                'idx': 1,
                'gl_PerVertex_var.gl_Position': [0.0, -0.5, 0.0, 1.0],
                'vertOut.pos': [0.0, -0.5, 0.0, 1.0],
                'vertOut.col': [0.0, 1.0, 0.0, 1.0],
                'vertOut.uv': [0.0, 1.0, 0.0, 1.0],
            },
            2: {
                'vtx': 2,
                'idx': 2,
                'gl_PerVertex_var.gl_Position': [0.5, 0.5, 0.0, 1.0],
                'vertOut.pos': [0.5, 0.5, 0.0, 1.0],
                'vertOut.col': [0.0, 1.0, 0.0, 1.0],
                'vertOut.uv': [1.0, 0.0, 0.0, 1.0],
            },
        }

        self.check_mesh_data(postvs_ref, postvs_data)
