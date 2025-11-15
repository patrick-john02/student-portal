<script lang="ts">
export const description = "Subjects management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import { Plus, MoreHorizontal } from "lucide-vue-next"

const userRole = "Admin"

// Dummy subjects data
const subjects = ref([
  {
    id: 1,
    name: "General Mathematics",
    code: "MATH-11",
    grade: "Grade 11",
    teacher: "Maria Santos",
    color: "bg-blue-500",
  },
  {
    id: 2,
    name: "Oral Communication",
    code: "ENG-11",
    grade: "Grade 11",
    teacher: "Juan Dela Cruz",
    color: "bg-green-500",
  },
  {
    id: 3,
    name: "Accountancy Fundamentals",
    code: "ABM-12",
    grade: "Grade 12",
    teacher: "Ana Reyes",
    color: "bg-yellow-500",
  },
  {
    id: 4,
    name: "Physical Education 2",
    code: "PE-12",
    grade: "Grade 12",
    teacher: "Robert Garcia",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header
        class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all"
      >
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Subjects</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Subjects</h2>
            <p class="text-sm text-muted-foreground">
              Manage academic subjects and assigned teachers.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Subject
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Subjects Overview</CardTitle>
            <CardDescription>
              View, edit, or remove academic subjects.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search subjects..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-56">Subject</TableHead>
                  <TableHead>Teacher</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="sub in subjects"
                  :key="sub.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Subject Info -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div
                        class="h-3 w-3 rounded-full"
                        :class="sub.color"
                      ></div>
                      <div>
                        <p class="font-medium">{{ sub.name }}</p>
                        <p class="text-xs text-muted-foreground">
                          {{ sub.code }}
                        </p>
                      </div>
                    </div>
                  </TableCell>

                  <!-- Teacher -->
                  <TableCell class="text-muted-foreground">
                    {{ sub.teacher }}
                  </TableCell>

                  <!-- Grade Level -->
                  <TableCell>
                    <Badge variant="secondary">
                      {{ sub.grade }}
                    </Badge>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>Edit Subject</DropdownMenuItem>
                        <DropdownMenuItem>Assign Teacher</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete Subject
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
