<template>
  <div class="hello">
    <template v-if="$store.state.isAuthenticated">
      <h1 class="title">Latest messages</h1>
      <div class="rows">
        <div class="todo">
          <div class="card" v-for="task in data" style="margin-bottom: 10px;">
            <!-- Loop through the tasks array, if status is 'todo' then we'll show it. -->
            <div class="card-content" data_id="{{$task->id}}">
              <div class="content" style="align-items: center;">
                <strong>From: </strong> {{ task.sender }} <span>
                  <button style="margin-left: 100px;" v-on:click="select(task.id)">🗑️</button> <br>
                </span>
                <strong>You: </strong> {{ task.recipent }} <br>
                <strong>Title: </strong>{{ task.title }} <br>
                Message: {{ task.message }} <br>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>

  </div>

</template>

<script>
// aloo
let user = localStorage.getItem('email');
export default {
  data() {
    return {
      data: [],
    };
  },
  methods: {
    async fetchData() {
      let response = await fetch("http://localhost:8000/api/inbox/"+user);
      this.data = await response.json();
    },
    select: async function (id) {
      console.log(id);
      let abc = await fetch("http://localhost:8000/api/delete_event/" + id).then(location.reload());

    },
  },
  mounted() {
    this.fetchData();
  },
    created(){
    this.interval = setInterval(() =>{
      this.fetchData()},10000)
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
