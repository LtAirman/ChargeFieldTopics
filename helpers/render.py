import ipywidgets as widgets
from ipywidgets import HBox, VBox, Button, ButtonStyle, GridspecLayout


def render_periodic_table(df):
    atomic_types = [
        "nonmetal",
        "noble_gas",
        "alkali_metal",
        "alkaline_earth",
        "metalloid",
        "halogen",
        "basic_metal",
        "transition_metal",
        "lanthanide",
        "actinide",
    ]

    # 10 atomic type colors
    atomic_type_colors = [
        "skyblue",
        "cyan",
        "tomato",
        "orange",
        "springgreen",
        "powderblue",
        "palegreen",
        "yellow",
        "thistle",
        "violet",
    ]

    type_color_dict = dict(zip(atomic_types, atomic_type_colors))

    df["allATypes"] = list(zip(df.AtomicNumber, df.AtomicType))
    ATypes = df["allATypes"].drop_duplicates().array

    color_list = []
    for i in range(90):
        color_list.append(type_color_dict[ATypes[i][1]])

    atomic_symbols = df["AtomicSymbol"].drop_duplicates().array

    a_buttons = []
    for i in range(90):
        button = Button(
            description=atomic_symbols[i], style=dict(button_color=color_list[i])
        )
        button.layout = widgets.Layout(border="1px solid black")
        button.layout.width = "100%"
        button.layout.height = "100%"  #'40px'
        a_buttons.append(button)

    grid = GridspecLayout(10, 18)
    grid[0, 0] = a_buttons[0]
    grid[0, 17] = a_buttons[1]
    grid[1, 0] = a_buttons[2]
    grid[1, 1] = a_buttons[3]

    for p in range(12, 18):
        grid[1, p] = a_buttons[p - 8]

    grid[2, 0] = a_buttons[10]
    grid[2, 1] = a_buttons[11]

    for n in range(12, 18):
        grid[2, n] = a_buttons[n]

    for m in range(18):
        grid[3, m] = a_buttons[18 + m]

    for k in range(18):
        grid[4, k] = a_buttons[36 + k]

    grid[5, 0] = a_buttons[54]
    grid[5, 1] = a_buttons[55]
    # grid[5,2] = the Lanthanide series hole

    for i in range(3, 18):
        grid[5, i] = a_buttons[68 + i]

    grid[6, 0] = a_buttons[86]
    grid[6, 1] = a_buttons[87]
    # grid[6,2] = the Actinide series hole

    for j in range(2, 17):
        # Lanthanide series
        grid[7, j] = a_buttons[54 + j]
    # Actinide series
    grid[8, 2] = a_buttons[88]
    grid[8, 3] = a_buttons[89]

    # The periodic table button functions
    output = widgets.Output()


    return grid, color_list, a_buttons


def render_control_panel(elements):
    selectAtom = widgets.Dropdown(
        options=elements,
        value=2,
        description="Atom:",
    )
    atoms_label = widgets.Checkbox(
        value=False, description="Atomic label", disabled=False, indent=False
    )
    emission_type = widgets.Dropdown(
        options=["plane", "cones"],
        value="plane",
        description="Emission:",
    )
    include_neutrons = widgets.Checkbox(
        value=True, description="Show neutrons", disabled=False, indent=False
    )
    colored_emissions = widgets.Checkbox(
        value=False,
        description="Color emissions",
        disabled=False,
        indent=False,
    )
    # Changes the equatorial(or cone) emission radius
    emRSlider = widgets.FloatSlider(
        value=5.0,
        min=2.0,
        max=8.0,
        step=0.1,
        description="Emission Radius",
    )
    # Changes the distance tween adjacent orthogonal protons (or protonstacks)
    s1s2Slider = widgets.FloatSlider(
        value=2.5,
        min=2.0,
        max=3.0,
        step=0.01,
        description="o-slots gap",
    )
    # Changes the pole to pole distance between adjacent e-p-n's
    p2p3Slider = widgets.FloatSlider(
        value=3.0,
        min=2.0,
        max=4.0,
        step=0.01,
        description="epn gap",
    )
    # Changes the neutron orbital radius
    nOSlider = widgets.FloatSlider(
        value=4.0,
        min=2.0,
        max=6.0,
        step=0.1,
        description="N offset",
    )
    # Changes the cone emission angle
    coneAngleSlider = widgets.FloatSlider(
        value=30,  # deg
        min=20,
        max=40,
        step=0.1,
        description="Cone angle",
    )
    camera_type = widgets.Dropdown(
        options=["orthographic", "perspective"],
        value="perspective",
        description="View:",
    )
    camera_type2 = widgets.Dropdown(
        options=["horizontal", "vertical"],
        value="vertical",
        description="Z Axis:",
    )

    # The guiwidget control panel
    guiwidgets = widgets.VBox(
        [
            selectAtom,
            atoms_label,
            emission_type,
            colored_emissions,
            include_neutrons,
            emRSlider,
            s1s2Slider,
            p2p3Slider,
            nOSlider,
            coneAngleSlider,
            camera_type,
            camera_type2,
        ]
    )

    # Observe any changes in widget values, button or gui
    selected_atomic_number = selectAtom.value

    def handle_change(change):
        global number
        number = change.new

    selectAtom.observe(handle_change, "value")

    display_neutrons = include_neutrons.value

    def handle_change(change):
        global display_neutrons
        display_neutrons = change.new

    include_neutrons.observe(handle_change, "value")

    emission_radius = emRSlider.value

    def handle_change(change):
        global emR
        emR = change.new

    emRSlider.observe(handle_change, "value")

    s1s2 = s1s2Slider.value  # Dist tween 2 ortho protons

    def handle_change(change):
        global s1s2
        s1s2 = change.new

    s1s2Slider.observe(handle_change, "value")

    p2p3Dist = p2p3Slider.value  # between adjacent e-p-n's

    def handle_change(change):
        global p2p3Dist
        p2p3Dist = change.new

    p2p3Slider.observe(handle_change, "value")

    neutron_orbit_radius = nOSlider.value  # between adjacent e-p-n's

    def handle_change(change):
        global neutron_orbit_radius
        neutron_orbit_radius = change.new

    nOSlider.observe(handle_change, "value")

    c_angle_degree = coneAngleSlider.value  # cone angle

    def handle_change(change):
        global c_angle_degree
        c_angle_degree = change.new

    coneAngleSlider.observe(handle_change, "value")

    camera_mode = camera_type.value

    def handle_change(change):
        global cameraMode
        cameraMode = change.new

    camera_type.observe(handle_change, "value")

    camera_orient = camera_type2.value

    def handle_change(change):
        global cameraOrient
        cameraOrient = change.new

    camera_type2.observe(handle_change, "value")

    return (
        guiwidgets,
        selected_atomic_number,
        display_neutrons,
        colored_emissions,
        emission_type,
        emission_radius,
        s1s2,
        p2p3Dist,
        neutron_orbit_radius,
        c_angle_degree,
        camera_mode,
        camera_orient,
        camera_type,
        atoms_label,
        selectAtom
    )
