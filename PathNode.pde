class PathNode {

  LinkedList<PathNode> edges = new LinkedList<PathNode>();//all the nodes this node is connected to 
  float x;
  float y;
  float smallestDistToPoint = 10000000;//the distance of smallest path from the start to this node 
  int degree;
  int value;  
  boolean checked = false;
  boolean isGhost = false;
  //-------------------------------------------------------------------------------------------------------------------------------------------------
  //constructor
  PathNode(float x1, float y1) {
    x = x1;
    y = y1;
  }
  PathNode(PVector vec) {
    x = vec.x;
    y = vec.y;
  }


  PathNode(PVector vec, boolean doesNothing) {
    x = vec.x;
    y = vec.y;
    isGhost = true;
  }
  //-------------------------------------------------------------------------------------------------------------------------------------------------
  //draw a litle circle
  void show() {
    fill(0, 100, 100);
    PVector pixel = tileToPixel(new PVector(x,y));
    ellipse(pixel.x, pixel.y,10,10);
  }

  //-------------------------------------------------------------------------------------------------------------------------------------------------
  //add all the nodes this node is adjacent to 
  void addEdges(ArrayList<PathNode> nodes) {
    for (int i =0; i < nodes.size(); i++) {//for all the nodes
      if (nodes.get(i).y == y ^ nodes.get(i).x == x) {
        if (nodes.get(i).y == y) {//if the node is on the same line horizontally
          float mostLeft = min(nodes.get(i).x, x) + 1;
          float max = max(nodes.get(i).x, x);
          boolean edge = true;
          while (mostLeft < max) {//look from the one node to the other looking for a wall

            if (originalTiles[(int)y][(int)mostLeft].wall) {
              edge = false;//not an edge since there is a wall in the way
              break;
            }
            mostLeft ++;//move 1 step closer to the other node
          }
          if (edge) {
            edges.add(nodes.get(i));//add the node as an edge
          }
        } else if (nodes.get(i).x == x) {//same line vertically
          float mostUp = min(nodes.get(i).y, y) + 1;
          float max = max(nodes.get(i).y, y);
          boolean edge = true;
          while (mostUp < max) {

            if (originalTiles[(int)mostUp][(int)x].wall) {
              edge = false;
              break;
            }
            mostUp ++;
          }
          if (edge) {
            edges.add(nodes.get(i));
          }
        }
      }
    }
  }

  PathNode clone() {
    PathNode clone = new PathNode(x, y); 
    clone.isGhost = isGhost;
    return clone;
  }
}