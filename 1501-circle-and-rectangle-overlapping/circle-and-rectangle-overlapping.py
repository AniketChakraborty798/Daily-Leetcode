class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Clamp center coordinates to rectangle bounds to find closest point
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        
        # Distance squared from center to closest point
        dx = xCenter - closestX
        dy = yCenter - closestY
        
        return dx * dx + dy * dy <= radius * radius