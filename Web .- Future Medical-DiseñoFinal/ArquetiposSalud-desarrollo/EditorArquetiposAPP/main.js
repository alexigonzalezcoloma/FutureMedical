const { app, BrowserWindow, Menu, ipcMain } = require('electron');

const url = require('url');
const path = require('path');

let mainWindow;
let newProductWindow;

// Recargar mientras editas archivos, sin necesidad de abrir la app denuevo
require('electron-reload')(__dirname, { electron: require(`${__dirname}/node_modules/electron`) });


app.on('ready', () => {

	// Ventana principal
	mainWindow = new BrowserWindow({width: 1275, height: 720});

	mainWindow.loadURL(url.format({
    	pathname: path.join(__dirname, 'src/index.html'),
    	protocol: 'file',
    	slashes: true,
  	}))

  	// Menu
  	const mainMenu = Menu.buildFromTemplate(templateMenu);
  	Menu.setApplicationMenu(mainMenu);

  	// Si cerramos la ventana, la aplicacion se cierra
  	mainWindow.on('closed', () => {
    	app.quit();
  	});

});

// Menu superior con opciones (Archivo, Ayuda, Salir)
const templateMenu = [
  	{
    	label: 'Archivo',
    	submenu: [
      		{
        		label: 'Archivo',
        		accelerator: 'Ctrl+N',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Remove All Products',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Exit',
        		accelerator: process.platform == 'darwin' ? 'command+Q' : 'Ctrl+Q',
        		click() {
          			app.quit();
        		}
      		}	
    	]
    },

    {
    	label: 'Editar',
    	submenu: [
      		{
        		label: 'Archivo',
        		accelerator: 'Ctrl+N',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Remove All Products',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Exit',
        		accelerator: process.platform == 'darwin' ? 'command+Q' : 'Ctrl+Q',
        		click() {
          			app.quit();
        		}
      		}	
    	]
  	},

  	{
    	label: 'Ver',
    	submenu: [
      		{
        		label: 'Archivo',
        		accelerator: 'Ctrl+N',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Remove All Products',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Exit',
        		accelerator: process.platform == 'darwin' ? 'command+Q' : 'Ctrl+Q',
        		click() {
          			app.quit();
        		}
      		}	
    	]
  	},

  	{
    	label: 'Ayuda',
    	submenu: [
      		{
        		label: 'x',
        		accelerator: 'Ctrl+N',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Remove All Products',
        		click() {
          			
        		}
      		},
      		{
        		label: 'Exit',
        		accelerator: process.platform == 'darwin' ? 'command+Q' : 'Ctrl+Q',
        		click() {
          			app.quit();
        		}
      		}	
    	]
  	}
];