import App from './App.svelte';

const app = new App({
	target: document.querySelector('#client'),
	props: {
		name: 'Team 4'
	}
});

export default app;