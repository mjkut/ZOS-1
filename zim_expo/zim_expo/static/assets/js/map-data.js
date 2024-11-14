

// Initialize the map and set its view to Zimbabwe
const map = L.map('map').setView([-19.0154, 29.1549], 6); // Zimbabwe's approximate center



// Dark-themed tile layer
const darkTileLayer = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://carto.com/">CARTO</a>',
    maxZoom: 18,
}).addTo(map);

// Optional Satellite tile layer
const satelliteTileLayer = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://opentopomap.org/">OpenTopoMap</a> contributors',
    maxZoom: 17,
});

// Add the OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Tourist Attractions Data
const attractions = [
   // Harare
   { name: "Harare National Gallery", location: [-17.8292, 31.0536], description: "A showcase of Zimbabwean art and culture." },
   { name: "National Heroes Acre", location: [-17.8615, 31.0212], description: "A national monument and burial ground for Zimbabwe's liberation heroes." },
   { name: "Mukuvisi Woodlands", location: [-17.8489, 31.0736], description: "A wildlife sanctuary with indigenous flora and fauna." },
   { name: "The Kopje", location: [-17.8341, 31.0439], description: "A granite hill offering panoramic views of Harare." },

   // Bulawayo
   { name: "Bulawayo Railway Museum", location: [-20.1530, 28.5764], description: "Museum preserving Zimbabwe's railway heritage." },
   { name: "Natural History Museum", location: [-20.1618, 28.5888], description: "One of Africa’s best museums, showcasing natural and cultural history." },
   { name: "Lumene Falls", location: [-19.7635, 27.8962], description: "Scenic waterfall near Bulawayo." },

   // Masvingo
   { name: "Lake Mutirikwi", location: [-20.2333, 30.8428], description: "Popular for fishing, boating, and scenic views." },
   { name: "Great Zimbabwe", location: [-20.2674, 30.9335], description: "Ancient city ruins and UNESCO World Heritage Site." },
   { name: "Gonarezhou National Park", location: [-21.3596, 31.8777], description: "One of Zimbabwe's largest national parks, home to diverse wildlife." },

   // Manicaland
   { name: "Mutarazi Falls", location: [-18.2442, 32.7534], description: "Zimbabwe's highest waterfall, located in the Eastern Highlands." },
   { name: "Vumba Mountains", location: [-19.0707, 32.7505], description: "A mountain range offering lush landscapes and stunning views." },
   { name: "Bridal Veil Falls", location: [-19.1229, 32.8255], description: "A scenic waterfall near Chimanimani." },
   { name: "Pungwe Falls", location: [-18.3128, 32.7016], description: "A beautiful waterfall in Nyanga National Park." },

   // Mashonaland East
   { name: "Imire Game Park", location: [-17.8554, 31.6083], description: "Wildlife sanctuary known for rhino conservation." },

   // Mashonaland West
   { name: "Mana Pools National Park", location: [-15.7402, 29.3614], description: "UNESCO World Heritage Site and wildlife-rich floodplain." },
   { name: "Lake Kariba Recreational Park", location: [-16.5164, 28.8002], description: "One of the world's largest man-made lakes, popular for water sports." },
   { name: "Chinhoyi Caves", location: [-17.3575, 30.1761], description: "Limestone caves with clear blue pools, perfect for diving." },

   // Mashonaland Central
   { name: "Domboshava Caves", location: [-17.5761, 31.1453], description: "Granite hill with ancient rock paintings." },

   // Midlands
   { name: "Antelope Park", location: [-19.4278, 30.1053], description: "A wildlife sanctuary offering unique animal encounters." },
   { name: "Zimbabwe Military Museum", location: [-19.4585, 29.8225], description: "Museum showcasing Zimbabwe's military history." },

   // Matabeleland North
   { name: "Victoria Falls", location: [-17.9243, 25.8565], description: "One of the Seven Natural Wonders of the World." },
   { name: "Hwange National Park", location: [-18.7353, 26.9525], description: "Zimbabwe's largest national park, famous for its elephants." },
   { name: "Zambezi National Park", location: [-17.9243, 25.8587], description: "A diverse park along the Zambezi River." },
   { name: "Victoria Falls Bridge", location: [-17.9253, 25.8572], description: "Iconic bridge connecting Zimbabwe and Zambia." },

   // Matabeleland South
   { name: "Threeways Safari", location: [-21.1622, 29.2635], description: "Popular safari destination in the south." },
   { name: "Nottingham Estates", location: [-21.3921, 29.3156], description: "Scenic estate offering fishing and wildlife viewing." },
   { name: "The Great Limpopo Transfrontier Conservation Area", location: [-22.4167, 31.4167], description: "Conservation area linking Zimbabwe, Mozambique, and South Africa." },
];

// Add markers to the map for each attraction
attractions.forEach(attraction => {
    L.marker(attraction.location)
        .addTo(map)
        .bindPopup(`<b>${attraction.name}</b><br>${attraction.description}`);
});