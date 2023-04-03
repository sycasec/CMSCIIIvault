# Image Processing Lecture Video

```toc
```

## Course Summary
- the automated processing and analysis of imagery is becoming highly important
- the course is intended to provide an introduction to image processing
- learner should be able to tackle common image processing and analysis problems, such as de-noising, enhancement, detection, segmentation, and classification.

## The 3 layers of Image Understanding
- Image Processing → Enhanced Imagery for visual inspection
- Image Analysis → object detection, measurement, classification
- Machien Vision → object recognition, scene understanding, 3d reconstruction 


## Imaging Sensors
- Optical
	- still frame & video cameras
	- document scanners
	- hyperspectral
- Radar
	- SAR, ISAR, navigation imagery
- Medical
	- Xray, CT, MRI
	- Ultrasonic
- Other
	- Flash LADAR, Xbox Kinect, Depth imagery

### Optical Sensors
- Visual band
	- digital still cameras
		- 2d CCD/CMOS arrays
	- Video
		- digital capture → analogue output
		- digital → digital (webcams, DV cam, HDTV)
		- legacy – analogue vacuum imaging tubes
	- Infra-red
		- near/far IR bands
			- day/night capability
	- specialized devices

#### The Human Eye
- contains photo receptors
- has daytime vision and night/lowlight vision

#### Typical Optical Camera
- Lens Iris CCD array (focal plane), signal processing unit
- extension of the simple pin-hole camera
- light focused down on to the focal plane by a combination of lenses
- image on focal plane recorded either on film or CCD array sensor
- In digital camera the image data is post processed prior to storage (compressed?)

#### Optical Cameras - Lenses & Focusing
- to allow greater light in lenses used to focus image onto focal plane
- increased light at cost of limited depth of field
- depending on lens type/quality, image may be out of focus at edges
- lens distortion present for wide angle views
- optical artefacts can also be caused by refraction of different wavelengths  
![[Pasted image 20230222222756.png|400]]

#### Optical Cameras - Depth of Field vs Aperture
- narrow aperture → dim image
- wide aperture → bright image
- aperture size usually given in terms of f-stops (f3.5, f8, f11, etc…)
- narrower aperture better approximates pinhole camera (sharper picture overall)
- good SNR (bright image) required for good image capture in low light
- may require longer exposure integration time of good depth of field required
- ![[Pasted image 20230222222946.png|350]]

#### Optical Sensor Arrays - resolution and observability (contains eq)
$$h \approx pd\frac{2}{n}tan(\frac{f^{\circ}}{2}\frac{\pi}{180})$$
- `n` → the number of array elements (n x n)
- $f^\circ$ → field of view
- $d$ → distance to the object
- $h$ → object height
- $p$ → number of pixels the object spans in the image

## Charged Couple Device (CCD Array)
![[Pasted image 20230222224521.png|525]]
- Photons converted into an accumulated electric charge in each cell
- image is read off by shifting charge row by row into a voltage converter
- charge is moved acros chip, amplified, and converted to an analogue voltage

## CMOS Array (complementary metal-oxide-semiconductor)
- reffered to as an active pixel sensor where each pixel detector (photo diode) has a local amplifier
- photons again converted into an accumulated electric charge in each cell
- charge is locally amped then transferred to A/D registers
- less expensive than CCD but loss in area of each pixel (also low power, less sensitive to bloom, more sensitive to noise)
- commonly used in digicams or phones

## Typical on-camera processing steps
![[Pasted image 20230222224803.png|700]]

## CCD Colour Imagery - Bayer Patterns
- split light across 3 separate sensors or use a bayer pattern of RGB micro-lenses 
- full color image is reconstruction (de-mosaicing) of sub-sampled dataset
- ![[Pasted image 20230222224920.png|325]]

### Simple Bayer Pattern Reconstruction (demosaicing)
![[Pasted image 20230222225018.png|675]]
- simple recons can introduce unwanted colour artefacts near sharp edges
- more complex reconstruction techniques are employed to solve these problems

## Other Filter Patterns
![[Pasted image 20230222225120.png|600]]

