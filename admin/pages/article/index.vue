<template>
  <section>
    <el-button type="danger"><a @click="$router.push({name:'article-add'})">add Article</a></el-button>
    <h3>記事一覧</h3>
    <el-row>
      <el-col :span="6" v-for="article in articles" :key="article.id">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="article.image" class="image">
          <div style="padding: 14px;">
            <span><a @click="$router.push({name:'article-id', params:{id:article.id}})"><el-button type="primary">{{article.title}}</el-button></a></span>
            <span><a @click="$router.push({name:'article-edit', params:{id:article.id}})"><el-button type="warning">編集</el-button></a></span>
            <span><el-button @click="onDelete(article.id)" type="danger">削除</el-button></span>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </section>
</template>

<script>
  export default{
    data() {
      return {
        articles: [],
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('article/')
        this.articles = res
      },
      // onDelete: function(index){
      //   this.articles.splice(index, 1);
      // }
      async onDelete(article_id) {
        try {
          await this.$axios.$delete(`article/${article_id}/`); // delete article
          let newArticles = await this.$axios.$get("/article/"); // get new list of articles
          this.articles = newArticles; // update list of articles
        } catch (e) {
          console.log(e);
        }
      }
    }
  }
</script>
<style>
  .recipe-card {
      box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
  }
    .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    height: 200px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>
