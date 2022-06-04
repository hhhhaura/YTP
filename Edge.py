import numpy as np
import cv2 as cv
from Puzzle.Enums import TypeEdge, Directions
# add this
def comp(a, b):
    return abs(a - b) <= 0.000000001
class Edge:
    """
        Wrapper for edges.
        Contains shape, colors, type and positions informations in the puzzle of an edge.
    """

    def __init__(self, shape, color, type=TypeEdge.HOLE, connected=False, direction=Directions.N):
        self.shape = shape
        self.shape_backup = shape
        self.color = color
        self.type = type
        self.connected = connected
        self.direction = direction
    #new function
    def change(self, to) :
        self.shape = to.shape
        self.shape_backup = to.shape_backup
        self.color = to.color
        self.type = to.type
        self.direction = to.direction
    # hash
    def __hash__(self):
        return 1
    def __eq__(self, other) :
        yes = True
        yes = yes and (comp(cv.matchShapes(self.shape, other.shape, 1, 0.0), 0.0))
        return yes
        
    def is_border(self, threshold):
        """
            Fast check to determine of the edge is a border.

            :param threshold: distance threshold
            :return: Boolean
        """

        def dist_to_line(p1, p2, p3):
            return np.linalg.norm(np.cross(p2 - p1, p1 - p3)) / np.linalg.norm(p2 - p1)

        total_dist = 0
        for p in self.shape:
            total_dist += dist_to_line(self.shape[0], self.shape[-1], p)
        return total_dist < threshold

    def backup_shape(self):
        """ Copy the shape for backup """

        self.shape_backup = np.copy(self.shape)

    def restore_backup_shape(self):
        """ Restore the shape previously backedup """

        self.shape = self.shape_backup

    def is_compatible(self, e2):
        """ Helper to determine if two edges are compatible """

        return (self.type == TypeEdge.HOLE and e2.type == TypeEdge.HEAD) or (self.type == TypeEdge.HEAD and e2.type == TypeEdge.HOLE) \
               or self.type == TypeEdge.UNDEFINED or e2.type == TypeEdge.UNDEFINED
