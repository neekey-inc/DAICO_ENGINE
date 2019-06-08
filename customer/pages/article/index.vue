<template>
  <div>
    <table class="table">
      <tbody>
          <tr v-for="article in articles" :key="article.id">
              <td><a :href="'/article/' + article.id">{{article.title}}</a></td>
              <td>{{article.published_at | dateFormat}}</td>
              <td><el-button-group>
                  <el-button type="info" icon="el-icon-edit" @click="$router.push({name: 'article-edit-id', params: {id: article.id}})" size="small"></el-button>
                  <el-button type="danger" icon="el-icon-delete" @click="removeModel(article)" size="small"></el-button>
              </el-button-group></td>
          </tr>
      </tbody>
    </table>
    <div>
    </div>
    <span>
    </span>
    <div>
      代行ENGINEに登録しよう
      <el-button @click="$router.push({name: 'user-sign'})">会員登録する</el-button>
      <el-button @click="$router.push({name: 'about'})">代行ENGINEとは？</el-button>
    </div>
  </div>
</template>
<script>
  import moment from 'moment'
  export default {
    data () {
        return {
            articles: [],
        }
    },
    mounted () {
        this.fetchData()
    } ,
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('article/')
        this.articles = res
        console.log(this.articles)
        // return { articles: res };
      }
    }
  }
</script>
