import {createStore} from 'vuex';

export default createStore({
	state: () =>  ({
		tickets: []
	}),
	mutations: {
		setFetchedTickets(state, tickets) {
			state.tickets = tickets
		}
	},
	actions: {
		async fetchTickets(ctx) {
			try {
				const ans = await fetch('http://127.0.0.1:8000/api/appeal', {method: 'GET'})
				const res = await ans.json()
				ctx.commit('setFetchedTickets', res)
				console.log(res)
			} catch (e) {
				console.error(`Error during fetch in mount: ${e}`)
			}
		}
	}
})
