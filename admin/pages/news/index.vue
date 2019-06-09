<template>
  <section>
    <el-button type="primary"><a @click="$router.push({name:'news-add'})">add News</a></el-button>
    <h3>記事一覧</h3>
    <el-row>
      <el-col :span="6" v-for="news in newses" :key="news.id">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="news.image" class="image">
          <div style="padding: 14px;">
            <span><a @click="$router.push({name:'news-id', params:{id:news.id}})"><el-button type="primary">{{news.title}}</el-button></a></span>
            <span><a @click="$router.push({name:'news-edit', params:{id:news.id}})"><el-button type="warning">編集</el-button></a></span>
            <span><el-button @click="onDelete(news.id)" type="danger">削除</el-button></span>
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
        newses: [],
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('news/')
        this.newses = res
      },
      // onDelete: function(index){
      //   this.newses.splice(index, 1);
      // }
      async onDelete(news_id) {
        try {
          await this.$axios.$delete(`news/${news_id}/`); // delete news
          let newNewses = await this.$axios.$get("/news/"); // get new list of newses
          this.newses = newNewses; // update list of newses
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
