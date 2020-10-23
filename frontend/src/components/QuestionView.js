import React, { Component } from 'react';
import $ from 'jquery';

import '../stylesheets/App.css';
import Question from './Question';
import Search from './Search';
import { baseUrl } from '../config';

class QuestionView extends Component {
  constructor() {
    super();
    this.state = {
      questions: [],
      page: 1,
      totalQuestions: 0,
      categories: [],
      currentCategory: null,
    }
  }

  componentDidMount() {
    this.getQuestions();
  }

  getQuestions = () => {
    $.ajax({
      url: baseUrl + `/questions?page=${this.state.page}`,
      type: "GET",
      beforeSend: function (request) {
        request.setRequestHeader("Access-Control-Allow-Origin", "*");
      },
      success: (result) => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          categories: result.categories,
          currentCategory: result.current_category
        })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
  }

  selectPage(num) {
    this.setState({ page: num }, () => this.getQuestions());
  }

  createPagination() {
    let pageNumbers = [];
    let maxPage = Math.ceil(this.state.totalQuestions / 10)
    for (let i = 1; i <= maxPage; i++) {
      pageNumbers.push(
        <span
          key={i}
          className={`page-num ${i === this.state.page ? 'active' : ''}`}
          onClick={() => { this.selectPage(i) }}>{i}
        </span>)
    }
    return pageNumbers;
  }

  getByCategory = (id) => {
    $.ajax({
      url: baseUrl + `/categories/${id}/questions`,
      type: "GET",
      success: (result) => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          currentCategory: result.current_category
        })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
  }

  submitSearch = (searchTerm) => {
    $.ajax({
      url: baseUrl + `/questions/search`,
      type: "POST",
      beforeSend: function (request) {
        request.setRequestHeader("Access-Control-Allow-Origin", "*");
      },
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({ query: searchTerm }),
      crossDomain: true,
      success: (result) => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          currentCategory: result.current_category
        })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
  }

  questionAction = (id) => (action) => {
    if (action === 'DELETE') {
      if (window.confirm('are you sure you want to delete the question?')) {
        $.ajax({
          url: baseUrl + `/questions/${id}`,
          type: "DELETE",
          beforeSend: function (request) {
            request.setRequestHeader("Access-Control-Allow-Origin", "*");
          },    
          success: (result) => {
            this.getQuestions();
          },
          error: (error) => {
            alert('Unable to load questions. Please try your request again')
            return;
          }
        })
      }
    }
  }

  render() {
    const categories = this.state.categories
    const questions = this.state.questions

    return (
      <div className="question-view">
        <div className="categories-list">
          <h2 onClick={() => { this.getQuestions() }}>Categories</h2>
          <ul>
            {categories.map(element => {
              const imageUrl = element.type.toLowerCase() + '.svg'
              return (
                <li className="category-item" key={element.id} onClick={() => this.getByCategory(element.id)}>
                  <img className="category" alt="" src={imageUrl} />
                  {element.type}
                </li>
              )
            })}
          </ul>
          <Search submitSearch={this.submitSearch} />
        </div>
        <div className="questions-list">
          <h2>{this.state.totalQuestions}{' '}Questions</h2>
          {questions.map(q => {
            const category = categories.filter(c => c.id === q.category)[0]
            return (
              <Question
                key={q.id}
                question={q.question}
                answer={q.answer}
                category={category}
                difficulty={q.difficulty}
                questionAction={this.questionAction(q.id)}
              />
            )
          })}
          <div className="pagination-menu">
            {this.createPagination()}
          </div>
        </div>

      </div>
    );
  }
}

export default QuestionView;
