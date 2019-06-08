<template>
  <div>
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="タイトル">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="カテゴリ">
        <el-select v-model="form.category" placeholder="カテゴリを選択してください">
          <el-option label="Zone one" value="shanghai"></el-option>
          <el-option label="Zone two" value="beijing"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="公開日">
        <el-date-picker type="date" placeholder="Pick a date" v-model="form.published_at" style="width: 100%;"></el-date-picker>
      </el-form-item>
      <el-form-item label="本文">
        <el-input type="textarea" v-model="form.detail"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="save">保存</el-button>
        <el-button>キャンセル</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import moment from 'moment'
  import axios from 'axios'
  export default {
    data() {
      return {
        form: {
          title: '',
          category: '',
          published_at: '',
          detail: ''
        }
      }
    },
    methods: {
      save() {
        let self = this
        let post_data = {
            title: this.form.title,
            category: this.form.category,
            published_at: this.form.published_at,
            detail: this.form.detail,
        }
        if (this.form.published_at) {
          post_data.published_at = moment(this.form.published_at).format('YYYY-MM-DD')
        }

        console.log(post_data)
        let url = 'article/'
        self.loading = true
        this.$axios['post'](url, post_data).then(response => {
            self.$message('保存が完了しました')
            self.loading = false
        }).catch(error => {
            if (error.response) {
                let e = error.response.data
                self.$message('失敗')
            }
        })
        // axios.post('article/', post_data).then(response => {
        //   console.log(post_data)
        //   self.$message('保存が完了しました')
        //   self.loading = false
        //   })
      }
    }
  }
</script>
