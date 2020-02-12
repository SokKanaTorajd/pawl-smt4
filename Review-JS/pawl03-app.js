// file: pawl03-app.js
// Aplikasi JavaScript

// data produk yg ditampilkan
var products = [
    {
        id: 1,
        name: 'Arsikom & Sistem Operasi',
        sks: 4,
        active: true, 
    },
    {
        id: 2,
        name: 'Pemrograman Basis Data',
        sks: 3,
        active: true, 
    },
    {
        id: 3,
        name: 'Rekayasa Perangkat Lunak',
        sks: 4,
        active: true, 
    },
    {
        id: 4,
        name: 'PAW Lanjutan',
        sks: 4,
        active: true, 
    },
    {
        id: 5,
        name: 'Arsitektur & Sistem Enterprise',
        sks: 4,
        active: false, 
    },
    {
        id: 7,
        name: 'Pengantar Statiska & Ilmu Data',
        sks: 4,
        active: false, 
    },
    {
        id: 8,
        name: 'Aljabar Linier',
        sks: 2,
        active: false, 
    },
    {
        id: 9,
        name: 'Jaringan Komputer & Komunikasi Data',
        sks: 2,
        active: false, 
    },
    {
        id: 10,
        name: 'Analisis Prose Bisnis',
        sks: 4,
        active: false, 
    },
    {
        id: 11,
        name: 'Sistem Manajemen Basis Data',
        sks: 4,
        active: false, 
    },
    {
        id: 12,
        name: 'Pengembalian Aplikasi Web',
        sks: 4,
        active: false, 
    },
    {
        id: 13,
        name: 'Pengantar E-Bisnis',
        sks: 4,
        active: false, 
    },
    {
        id: 14,
        name: 'Algoritma & Struktur Data',
        sks: 4,
        active: false, 
    },
];

var total = 0;
var $app = document.querySelector('.app');

// tampilkan judul
function renderTitle(container) {
    var $title = document.createElement('h1');
    $title.innerHTML = 'Mata Kuliah';
    container.appendChild($title);
}

function addTotal(product, total, isAdd) {
    if (isAdd) {
        total += product.sks;
    } else {
        total -= product.sks;
    }
    return total;
}

// tampilkan daftar 
function renderList(container, products) {
    var $orderList = document.createElement('ul');

    // buat elemen tiap produk lalu tambahkan ke daftar
    products.forEach(function(product) {
        var $product = document.createElement('li');
        var $productsks = document.createElement('span');

        $productsks.innerHTML = currency(product.sks);
        $product.innerHTML = product.name;
        $product.appendChild($productsks)

        $orderList.appendChild($product);

        // add event handler
        $product.addEventListener('click',function(event) {
            // isAdd utk menentukan opr berikutnya adlh
            // operasi penambahan atau pengurangan

            var isAdd = !hasClass($product, 'is-active');
            // tambah atau buang class is-active sesuai operasi yang dilakukan 
            if (isAdd) {
                addClass($product, 'is-active');
            } else {
                removeClass($product, 'is-active');
            }

            // hitung total yang baru dari fungsi addTotal
            total = addTotal(product, total, isAdd);

            // perbarui nilai total di HTML DOM
            var $total = document.querySelector('.total span');
            $total.innerHTML = currency(total);
        });
    });
    container.appendChild($orderList);
}
// tampilkan jumlah total
function renderTotalContainer(container, total) {
    var $totalContainer = document.createElement('div');
    addClass($totalContainer, 'total');

    $totalContainer.innerHTML = 'Total SKS: ';

    var $total = document.createElement('span');
    $total.innerHTML = currency(total);
    $totalContainer.appendChild($total);

    container.appendChild($totalContainer);
}

// tampilkan judul, daftar, dan jumlah total
renderTitle($app);
renderList($app, products);
renderTotalContainer($app, total);

// querySelectorAll utk mendapatkan semua DOM Node yg sesuai dg 
// selector yg diberikan. kemudian kita bisa menggunakan loop (forEach) untuk
// setiap DOM Node-nya

var $products = document.querySelectorAll('li');
$products.forEach(function($product, index) {
    if(index < 2) {
        $product.dispatchEvent(new Event('click'));
    }
});