
# Charge Field topics on Jupyter Notebook

The goal of this project is to introduce Jupyter Notebook users to 
Charge Field physics and the Unified Field theory, etc. developed 
by Miles Mathis. See,
***THE GREATEST STANDING ERRORS IN PHYSICS AND MATHEMATICS***
<http://milesmathis.com/index.html>
[Miles Mathis science site Homepage](http://milesmathis.com/index.html)

## The only true particles in nature are photons 

Photons are real spinning objects with mass and radii as small as 
10^(-27)m. Photons travel with both forward and angular momentum 
(e=mc^2) due to both the photon's forward and spin tangential 
motions at light speed velocities. Large numbers of traveling photons 
and resulting collions create both electric (due to the photon's 
linear momentum) and magnetic (due to the photon's angular momentum) 
fields. 
                               
All spinning matter larger than electrons such as protons, planets, 
suns or galaxies are comprised of, and constantly recycle, photons, 
thus creating the charge field. Electrons are also comprised of 
photons however electrons are too small and energetic to allow 
proper photon recycling like larger and slower proton matter.

## Charge recycling 
                        
All protons are constantly receiving and emitting photons. Photons 
can enter a proton from any direction but usually do so at the 
proton's spin axis poles. Protons can emit photons outward in any 
direction but are usually emitted from the higher spin angular 
momentum latitudes about the proton's equator. We perceive the 
intake of charge as an apparent force of attraction, while photon 
emissions create repulsion. 
                        
## Proton bonding
                               
Protons can "bond" in one of two ways, pole-to-pole, as in the 
Helium atom, (also called an alpha) or equator-to-pole, a charge flow 
male to female connection. An electron or two will be caught in the 
streams of charge entering the proton and must orbit the proton pole, 
like "circling a drain". Neutrons too are caught in the proton charge 
stream and also orbit the proton's pole and spin axis, away from the 
proton's high emission equatorial zone.
                                
![The Helium atom](/images/Helium2.png)

# Atom Builder.

Atom Builder renders a 3D charge field model of the atom (1-90) 
selected by the user. 

![Periodic table](/images/atomBPT.png)
                               
For the first atom run the notebook from the beginning, each cell 
in turn. The first output cells contain a brief markdown  
explanation and periodic table, next the main guiwidget controls 
are displayed. Select the desired atom from either the table or 
drop-down widget. For subsequent atoms start at the periodic 
table or widget controls.

![Slotlayout diagram](/images/slotlayout84b.png)

The next output is the Slotlayout description and diagram. The 
Slotlayout is a charge field answer to the standard periodic table.

+ All atoms can be described by the number of protons (0-6) in each 
of up to 19 slot positions. The main vertical up/down column slots
(1-7) begins with Hydrogen and Helium's center slot1 containing 1 
and 2 protons.

+ The 1-19 slot sequence order number is indicated by the left side 
number in the atomic configuration in the center and in the left 
and right side vertical columns.

+ The 2 vertical side columns' slot sequence shown is top left, then 
top right, then down one on the left, then down one on the right,
odd slot numbers on the left and even slots on the right.

+ The proton count for a given slot is indicated by the right side 
number in the center atomic configuration and side columns.

+ The vertical, | or horizontal --- characters between the two 
numbers indicate the direction of the protons' equatorial emission 
planes viewed edgewise, orthogonal to the proton's spin axis.

+ Slot 1 is connected to the four front(10,14)/back(11,15) left(9,13)
/right(8,12), directions which spins as a single group called the 
Carousel. Or refer to the directions as +/-x, +/-y, and main vertical 
column +/-z.

+ Hook slot positions: 16,17,18, and 19, are joined to the main 
up/down column at slots, 2 and 3.  

+ The seven center buttons in the bottom row contains the total 
protons per slot color legend.

+ The selected atom’s symbol and atomic number are in the bottom 
right corner.

Here's the charge field atomic model of Polonium for comparison. 

![Polonium, Po 84](/images/polonium84.png)

Next, spin controls are explained and displayed. The rendered atom 
is displayed between two sets of the 19 slot rotation controls for
user convenience. 

![19 Rotation widgets](/images/rot_widget_array.png)

Only a few of the larger atoms have all 19 slots occupied. Each 
object within each slot spins about the spin axis through the slot 
center at the same rate, which is not correct, yet it still provides 
a good idea how the atom spins.

Eventually, all protons, neutrons and electrons should spin at their 
own rates. If a slot is unoccupied, the corresponding slot rotation 
control has nothing to spin and will not do anything. Try to remember 
to stop any active rotations before selecting another large atom or 
things will slow way down.

Good enough to share on GitHub. Collaborative efforts are welcome.  

The reference's **SECTION 9: THE NUCLEUS** contains descriptions
and diagrams of charge channeling and charge recycling by the 
elements. A paper most relevant to Atom Builder is 
>**How to Build the Elements**. 
>Explaining the periodic table, with nuclear diagrams".  
<http://milesmathis.com/nuclear.pdf>
[How to Build the Elements](http://milesmathis.com/nuclear.pdf)

![The Chromium atom](/images/chromium24.png)

A composite view showing two different Chromium atom output choices.

#### Files

* AtomBuilder.ipynb was created using Jupyter Notebook 6.4.0.
The code needs to import: pythreejs for the graphics, IPython
for the display and ipywidget for the controls.

* README.md This README file was also written with Jupyter notebook.

* .ipynb_checkpoints folder. As I understand it. The .ipynb_checkpoints 
folder/directory amounts to a temporary backup file generated by the
Notebook user's manual save commands, allowing the user to revert to 
the previous saved command. Its included in the gitignore file. 

* .gitignore. Containing only .ipynb_checkpoints and sub directories.

* images folder. The folder contains two png files: Helium2, chromium24, 
slotlayout84, atomBPT, and rot_widget_array.png, all of which are used 
in this readme file.

* LICENSE.txt, As soon as possible, 
>"This project is licensed under the terms of the MIT license."

#### For discussion, 

For charge field discussion visit the forum at "Miles Mathis' Charge Field - Portal" 
<https://milesmathis.forumotion.com>.
This particular project is described in the
**Miles Periodic Table with Standard Periodic Table reference**
thread,
<https://milesmathis.forumotion.com/t634p75-miles-periodic-table-with-standard-periodic-table-reference#6702>.

#### Contributing

Miles Mathis' Charge Field ideas are free. This project is 
intended to be a Public Domain free and open source, Jupyter 
Notebook application example
https://jupyter.org/
developed from graphics examples found at pythreejs  
https://pythreejs.readthedocs.io/en/stable/examples/index.html
and widgets found at
https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html
following Miles Mathis' ideas.
http://milesmathis.com/index.html

This project was Cr6's idea. He's also responsible for following Miles 
Mathis' atomic model and creating the Slotlayout diagram on which this 
project greatly relies.

There's at least one 10 year old charge field javaScript "Atom Viewer" 
out there, Nevyn's object oriented, way sophisticated javaScript code. 
I guess I'm ready to try and figure it out. 

Please pardon my understandings, personal interpretations and mistakes.

Pull requests are welcome. For major changes, please open an issue 
first to discuss what you'd like to change.
