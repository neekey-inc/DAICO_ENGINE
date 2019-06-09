<template>
  <section>
    <h3>記事詳細</h3>
    <el-row :getter="20">
      <el-col :sm="16">
        <table>
          <tbody>
            <tr>
              <td>{{newses.title}}</td>
            </tr>
            <tr>
              <td><img :src="newses.image" class="card-img-top" ></td>
            </tr>
            <tr>
              <td>{{newses.text}}</td>
            </tr>
          </tbody>
        </table>
        <div>
          代行ENGINEに登録しよう
          <el-button type="primary" @click="$router.push({name: 'user-sign'})">会員登録する</el-button>
          <el-button type="primary" @click="$router.push({name: 'about'})">代行ENGINEとは？</el-button>
        </div>
      </el-col>
      <el-col :sm="4" :span="4">
        <h3>関連記事</h3>
        <div v-for="news in news_list" :key="news.id">
          <el-card :body-style="{ padding: '0px' }" v-if="news.category==newses.category">
            <img :src="news.image" class="image">
            <div style="padding: 14px;">
              <span><a @click="$router.push({name:'news-id', params:{id:news.id}})">{{news.title}}</a></span>
            </div>
          </el-card>
        </div>
      </el-col>
    </el-row>
  </section>
</template>

<script>
  export default{
    data() {
      return {
        newses: [],
        news_list: [],
        // category_list: [],
      }
    },
    mounted() {
      this.fetchData()
      this.allData()
      // this.categoryData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('news/'+encodeURIComponent(this.$route.params.id)+'/')
        this.newses = res
      },
      async allData() {
        let data = await this.$axios.$get('news/')
        this.news_list = data
      },
      // async categoryData() {
      //   let category = await this.$axios.$get('news/')
      //   this.category_list = category
        // computed: {
        //   remaining: function(category_list) {
        //     var count = 0;
        //     var todos = this.category_list;
        //     var length = todos.length;
        //     for(var i = 0; i < length; i++) {
        //       if(!todos[i].done) {
        //         count++;
        //       }
        //     }
        //     return count;
        //   }
        // }
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

  .card-img-top {
    width:1000px;
  }
</style>
