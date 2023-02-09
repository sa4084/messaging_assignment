<template>
    <div class="compose">
        <div class="rows">

            <div>

                <h2> New Message </h2>
                <!-- <form action="/compose" method="POST">

                <div class="form-group">
                    <label for="email">Sender Email address</label>
                    <input type="email" class="form-control" id="email" placeholder="name@example.com">
                </div>
                <div class="form-group">
                    <label for="title">Name</label>
                    <input type="text" class="form-control" id="title" placeholder="title" >
                </div>
                <div class="form-group">
                    <label for="message">Your message</label>
                    <textarea name="message" class="form-control" id="message" rows="3"
                        ></textarea>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary">Submit</button>
                </div>
            </form> -->
                <form @submit.prevent="CreatePost">

                    <div class="form-group">
                        <label for="email">Recipent Email address</label>
                        <input type="email" class="form-control" id="email" placeholder="name@example.com"
                            v-model="form.recipent">
                    </div>
                    <br>
                    <div class="form-group">
                        <label for="title">Name</label>
                        <input type="text" class="form-control" id="title" placeholder="title" v-model="form.title">
                    </div> <br>
                    <div class="form-group">
                        <label for="message">Your message</label>
                        <textarea name="message" class="form-control" id="message" rows="3"
                            v-model="form.message"></textarea>
                    </div> <br>
                    <div class="form-group">
                        <button class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>

        </div>
    </div>

</template>

<script>

import axios from 'axios';
export default {
    name: 'CreatePost',
    data() {
        return {
            form: {
                recipent: '',
                sender: localStorage.getItem('email'),
                title: '',
                message: '',
            }
        }
    },
    methods: {
        async CreatePost() {
            if (this.form.recipent === '') { alert('recipent is empty'); return None; }
            if (this.form.title === '') { alert('title is empty'); return None; }
            if (this.form.message === '') { alert('message is empty'); return None; }

            axios.post('/api/compose', this.form, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Accept': '*/*',
                }
            })
                .then((res) => {
                    //Perform Success Action
                    console.log(res);
                    window.location.href = "./.."
                })
                .catch((error) => {
                    // error.response.status Check status code
                    console.log(error);
                });
        }
    }
}
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
