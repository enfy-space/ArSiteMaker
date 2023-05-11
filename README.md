# AR Site Maker
A tool to create a website where 3D models can be viewed using AR technology.
You can make simple marker based AR site that can view 3D model. 
Simply specify the site name, 3D model file (.glb), and marker image (URL).
You can try demo project by accessing below QR code and holding up QR code a camera after site is loaded.
You have to allow camera access from demo site.

## How to install
ar-site-maker is available through pip and PyPi. You need python3.
```
pip install ar-site-maker
```
You can confirm installation by executing ar-site-maker command.
```
ar-site-maker 
```
You can show top page like this if ar-site-maker is successfully installed.
```
Ar Site Maker {version}
 Documentation is here https://github.com/enfy-space/ArSiteMaker
```

## Usage
Usage is very easy!
<br>
### Preparing File
What you have to prepare is below.
* <b>.glb file</b>
  Sorry! we don't support .gltf file yet 🥹.
  <br>Please make sure to your model is

  * located around center of coordinate:(0,0,0) 
  * smaller than cube with 1 meter on a side
  * not buried in plane (elevation=0)

* <b> marker image or site URL </b>
  <br>Generated site is marker-based AR so Object is appear on the marker.
  There are two-way to make marker. 
  
  * image : You can set your favorite image as marker. 
  We recommend as simple and square as image possible.
  * URL : If specify your site URL, ar-site-maker set QR-code as marker automatically.

### Command Usage
Basic usage of command is below. <br>
If you want to use your favorite image as marker
```
 ar-site-maker make <your project name> <glb file path> -i <image path>
```
If you want to use QR code of your site as marker
```
 ar-site-maker make <your project name> <glb file path> -u <url>
```
#### Options
* title

  The site title will be the same as the project name if not specified.
If you want to set title arbitrarily, you can use --site_title option like this.
  ```
  ar-site-maker make <your project name> <glb file path> -u <url> --site_title <title>
  ```

* scale

  If you want to adjust object scale, you can use --scale option like this.
  ```
  ar-site-maker make <your project name> <glb file path> -u <url> --scale <scale>
  ```
* animation

  If you want to add rotate animation to object, you can add -a (or --animation) option like this.
  ```
  ar-site-maker make <your project name> <glb file path> -u <url> -a 
  ```

of course! you can open help like this
```
  ar-site-maker make -h 
```

```

├── project name
│   ├── subdirectory1 
│   │   ├── file1 
│   │   └── file2 
│   ├── subdirectory2
│   ├── file3 
│   └── file4
└── README.md

```