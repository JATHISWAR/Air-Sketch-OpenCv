<h1> Air-Sketch-OpenCv </h1>
A sample project made using OpenCv to Draw Sketches in Air with different colours.
<br></br>

<h2>Procedure :</h2>

<h4>Step 1 : Implement Color picker and find the correct set of HSV values </h4>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%201.03.58%20PM.png" width="600" height="400"/>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%2011.25.07%20AM.png" width="600" height="400"/>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%208.57.04%20PM.png" width="600" height="400"/>
<br> </br>
<h4> The most desirable HSV value for any object is the region where only the object is shown white and rest of the other elements are black. </h4>
<br></br>
<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%208.57.41%20PM.png" width="600" height="400"/>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%208.57.56%20PM.png" width="600" height="400"/>

<br> </br>
<h4> Step 2: Detecting the contours of the given object and also finding the tip of the contour for Air-Sketch. </h4>
<br></br>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%2011.51.37%20PM.png" width="600" height="400"/>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%2011.52.49%20PM.png" width="600" height="400"/>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-30%20at%2011.58.33%20PM.png" width="500" height="600"/>

<br> </br>
<h4> Step 3:Implement Air-Sketch Method to find the consecutive points to draw circles according to the movement of object in camera. </h4>
<br></br>

<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-31%20at%2012.09.52%20AM.png" width="600" height="400"/>
<br> </br>
<h4> Step 4 : These consecutive circles allow you to sketch. Now draw using Air Sketch and Enjoy! </h4>
<br></br>
<img src="https://github.com/JATHISWAR/Air-Sketch-OpenCv/blob/main/Screenshot%202021-03-31%20at%2012.11.14%20AM.png" width="600" height="400"/>
